"""
MIT License.

Copyright (c) 2020 BobDotCom

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import datetime
import functools
import re
import sys

__all__ = (
    "IntervalConverter",
    "parse_interval",
)

from typing import Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:  # pragma: no cover
    from typing_extensions import Literal

Unit = Literal[
    "seconds",
    "minutes",
    "hours",
    "days",
    "weeks",
    "months",
    "years",
    "decades",
    "centuries",
]


class IntervalConverter:
    """A converter to parse user input representing an amount of time into :class:`datetime.datetime` and
    :class:`datetime.timedelta` objects.

    Parameters
    ----------
    input_string: :class:`str`
        A string (usually user input) to be converted.
    max_unit: Literal["seconds", "minutes", "hours", "days", "weeks", "months", "years", "decades", "centuries"]
        The maximum unit to convert to. Defaults to "centuries".
    """

    _pattern: Dict[Unit, List[str]] = {
        "seconds": ["seconds", "second", "secs", "sec", "s"],
        "minutes": ["minutes", "minute", "mins", "min", "m"],
        "hours": ["hours", "hour", "hrs", "hr", "h"],
        "days": ["days", "day", "dys", "dy", "d"],
        "weeks": ["weeks", "week", "wks", "wk", "w"],
        "months": ["months", "month", "mons", "mon", "mn"],
        "years": ["years", "year", "yrs", "yr", "y"],
        "decades": ["decade", "decades", "dcd", "dec"],
        "centuries": ["century", "centuries", "c", "cen"],
    }

    def __init__(
        self,
        input_string: str,
        max_unit: Unit = "centuries",
    ) -> None:
        self._now = datetime.datetime.now()
        self._input_string = input_string
        self._converted_string: str
        if max_unit not in self._pattern:
            raise ValueError(
                "Invalid unit. Must be one of: " + ", ".join(self._pattern.keys())
            )
        self._max_unit = max_unit
        self._parsed_data: Dict[str, Union[int, float]] = {}
        for unit in self._pattern:
            self._parsed_data[unit] = 0
            if unit == max_unit:
                break
        self._parse_input()

    @property
    def input_string(self) -> str:
        """A string (usually user input) to be converted."""
        return self._input_string

    def _data_val(self, unit: Unit) -> Union[int, float]:
        return self._parsed_data.get(unit, 0)

    def _parse_input(self) -> None:
        converted_string = self.input_string
        for entry, value in self._pattern.items():
            regex_pattern = r"(?<=[0-9])\s*(" + "|".join(value) + r")((?=\s)|$)"
            converted_string = re.sub(regex_pattern, entry, converted_string)
        split_string = converted_string.split(" ")
        for part in split_string:
            for form in self._parsed_data:
                if form in part:
                    to_add = part.replace(form, "")
                    if to_add.replace(".", "").isdigit():
                        self._parsed_data[form] += float(to_add)
        self._converted_string = converted_string

    @functools.lru_cache()
    def datetime_precise(self) -> datetime.datetime:
        """
        A precise converter that uses the current system time, and accounts for conditional changes such as leap years,
        and months with varying days.

        .. note::
            The return value of this method is cached, so it will always return the same value when called on the same
            instance. However, it may return a different result when called at different times across multiple objects.
            This is because the current system time when the parent object was created is used to calculate the result.

        Returns
        --------
        :class:`datetime.datetime`
            A datetime object representing the parsed time.
        """
        years, months = divmod(self._data_val("months") + self._now.month, 12)
        years += self._data_val("years")
        years += self._data_val("decades") * 10
        years += self._data_val("centuries") * 100

        if months == 0:
            months = 12
            years -= 1

        return self._now.replace(
            month=int(months),
            year=self._now.year + int(years),
        ) + datetime.timedelta(
            seconds=self._data_val("seconds"),
            minutes=self._data_val("minutes"),
            hours=self._data_val("hours"),
            days=self._data_val("days"),
            weeks=self._data_val("weeks"),
        )

    @functools.lru_cache()
    def datetime_relative(self) -> datetime.datetime:
        """
        A relative converter that doesn't take leap years into account and uses rounded values for months.

        .. note::
            It is almost always recommended to use :meth:`datetime_precise` instead.

        .. note::
            The return value of this method is cached, so it will always return the same value when called on the same
            instance. However, it may return a different result when called at different times across multiple objects.
            This is because the current system time when the parent object was created is used to calculate the result.

        Returns
        --------
        :class:`datetime.datetime`
            A datetime object representing the parsed time.
        """
        return self._now + self.timedelta_relative()

    @functools.lru_cache()
    def timedelta_precise(self) -> datetime.timedelta:
        """
        A precise converter that uses the current system time, and accounts for conditional changes such as leap years,
        and months with varying days.

        .. note::
            The return value of this method is cached, so it will always return the same value when called on the same
            instance. However, it may return a different result when called at different times across multiple objects.
            This is because the current system time when the parent object was created is used to calculate the result.

        Returns
        --------
        :class:`datetime.timedelta`
            A timedelta object representing the parsed amount of time.
        """
        return self.datetime_precise() - self._now

    @functools.lru_cache()
    def timedelta_relative(self) -> datetime.timedelta:
        """
        A relative converter that doesn't take leap years into account and uses rounded values for months.

        .. note::
            Unless you cannot rely on system time or need a static return value, you should use
            :meth:`timedelta_precise` instead.

        Returns
        --------
        :class:`datetime.timedelta`
            A timedelta object representing the parsed amount of time.
        """
        days = self._data_val("days")
        days += round(30.5 * (self._data_val("months") % 12))
        years = self._data_val("years")
        years += self._data_val("decades") * 10
        years += self._data_val("centuries") * 100
        years += self._data_val("months") // 12
        days += years * 365
        return datetime.timedelta(
            seconds=self._data_val("seconds"),
            minutes=self._data_val("minutes"),
            hours=self._data_val("hours"),
            days=days,
            weeks=self._data_val("weeks"),
        )


def parse_interval(interval: str, max_unit: Unit = "centuries") -> IntervalConverter:
    """
    A shortcut function for :class:`IntervalConverter`.

    Parameters
    -----------
    interval: :class:`str`
        The string to parse.
    max_unit: Literal["seconds", "minutes", "hours", "days", "weeks", "months", "years", "decades", "centuries"]
        The maximum unit to parse to. Defaults to ``"centuries"``.

    Returns
    --------
    :class:`IntervalConverter`
        A converter object.
    """
    return IntervalConverter(interval, max_unit)
