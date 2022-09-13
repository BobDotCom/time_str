"""
MIT License.

Copyright (c) 2021 BobDotCom

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
import re
import warnings

__all__ = (
    "convert",
    "Converter",
    "convert_str",
)

from typing import Dict, List, Optional, Union


class Converter:
    """A converter to convert a string to a :class:`datetime.timedelta` object.

    The convert method returns a :class:`datetime.timedelta` object

    Attributes
    -----------
    input_string: :class:`str`
        A string (usually user input) to convert to a :class:`datetime.timedelta` object.
        This can be set during initialization.
    """

    def __init__(self, input_string: str):
        self.input_string = input_string
        self.converted_string: Optional[str] = None
        self.split_string: List[str] = []
        self.pattern = {
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
        self.raw_output: Dict[str, Union[int, float]] = {
            "seconds": 0,
            "minutes": 0,
            "hours": 0,
            "days": 0,
            "weeks": 0,
            "months": 0,
            "years": 0,
            "decades": 0,
            "centuries": 0,
        }
        self.output: Optional[datetime.timedelta] = None

    def convert(self) -> datetime.timedelta:
        """
        The converter itself.

        Takes the string input from initialization and transforms it into a
        :class:`datetime.timedelta` object.

        Returns
        --------
        :class:`datetime.timedelta`
            The converted datetime.timedelta object.
        """

        self.converted_string = self.input_string
        for entry, value in self.pattern.items():
            regex_pattern = r"(?<=[0-9])\s*(" + "|".join(value) + r")((?=\s)|$)"
            self.converted_string = re.sub(regex_pattern, entry, self.converted_string)
        self.split_string = self.converted_string.split(" ")
        for entry in self.split_string:
            for form in self.raw_output:
                if form in entry:
                    to_add = entry.replace(form, "")
                    if to_add.replace(".", "").isdigit():
                        self.raw_output[form] += float(to_add)
        if self.raw_output["months"] > 12:
            self.raw_output["years"] += self.raw_output["months"] // 12
            self.raw_output["months"] %= 12
        self.raw_output["days"] += round(30.5 * self.raw_output["months"])
        self.raw_output["days"] += 365 * self.raw_output["years"]
        self.raw_output["days"] += 3650 * self.raw_output["decades"]
        self.raw_output["days"] += 36500 * self.raw_output["centuries"]
        self.output = datetime.timedelta(
            seconds=self.raw_output["seconds"],
            minutes=self.raw_output["minutes"],
            hours=self.raw_output["hours"],
            days=self.raw_output["days"],
            weeks=self.raw_output["weeks"],
        )
        return self.output


def convert_str(input_string: str) -> datetime.timedelta:
    """
    A shorter way to use the :class:`Converter`.

    Returns the :class:`datetime.timedelta` object

    Parameters
    -----------
    input_string: :class:`str`
        A string (usually user input) to convert to a :class:`datetime.timedelta` object
    Returns
    --------
    :class:`datetime.timedelta`
        The converted datetime.timedelta object.
    """

    output = Converter(input_string).convert()
    return output


def convert(input_string: str) -> datetime.timedelta:
    """
    An alias of :func:`convert_str`.

    .. deprecated:: 0.2.0
        The convert function is deprecated since 0.2.0 and will be removed in 1.0.0. Use convert_str instead.

    Parameters
    -----------
    input_string: :class:`str`
        A string (usually user input) to convert to a :class:`datetime.timedelta` object
    Returns
    --------
    :class:`datetime.timedelta`
        The converted datetime.timedelta object.
    """
    warnings.warn(
        "The convert function is deprecated since 0.2.0 and will be removed in 1.0.0. Use convert_str instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    return convert_str(input_string)
