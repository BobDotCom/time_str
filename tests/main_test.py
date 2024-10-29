import datetime
import random

import pytest

import time_str
from time_str import IntervalConverter

maxes = (
    62,
    62,
    26,
    367,
    6,
    14,
    101,
    101,
    11,
)


def make_value() -> tuple[int, ...]:
    return (
        random.randrange(0, maxes[0]),
        random.randrange(0, maxes[1]),
        random.randrange(0, maxes[2]),
        random.randrange(0, maxes[3]),
        random.randrange(0, maxes[4]),
        random.randrange(0, maxes[5]),
        random.randrange(0, maxes[6]),
        random.randrange(0, maxes[7]),
        random.randrange(0, maxes[8]),
    )


tests = [make_value() for _ in range(1000)]


def precise_conversion(
    converter, second, minute, hour, day, week, month, year, decade, century
):
    years, months = divmod(converter._now.month + month, 12)
    years += year
    years += decade * 10
    years += century * 100

    if months == 0:
        months = 12
        years -= 1

    return converter._now.replace(
        month=int(months),
        year=converter._now.year + int(years),
    ) + datetime.timedelta(
        seconds=second,
        minutes=minute,
        hours=hour,
        days=day,
        weeks=week,
    )


@pytest.fixture
def converter():
    """Returns a converter."""
    return time_str.parse_interval


@pytest.mark.parametrize("second,minute,hour,day,week,month,year,decade,century", tests)
def test_conversions(
    converter, second, minute, hour, day, week, month, year, decade, century
):
    result = converter(
        f"{second} {random.choice(['seconds', 'second', 'secs', 'sec', 's'])} "
        f"{minute} {random.choice(['minutes', 'minute', 'mins', 'min', 'm'])} "
        f"{hour} {random.choice(['hours', 'hour', 'hrs', 'hr', 'h'])} "
        f"{day} {random.choice(['days', 'day', 'dys', 'dy', 'd'])} "
        f"{week} {random.choice(['weeks', 'week', 'wks', 'wk', 'w'])} "
        f"{month} {random.choice(['months', 'month', 'mons', 'mon', 'mn'])} "
        f"{year} {random.choice(['years', 'year', 'yrs', 'yr', 'y'])} "
        f"{decade} {random.choice(['decade', 'decades', 'dcd', 'dec'])} "
        f"{century} {random.choice(['century', 'centuries', 'c', 'cen'])}"
    )
    relative = datetime.timedelta(
        seconds=second,
        minutes=minute,
        hours=hour,
        days=day
        + round(30.5 * (month % 12))
        + (365 * (year + (month // 12)))
        + 7 * week
        + 3650 * decade
        + 36500 * century,
    )
    assert result.timedelta_relative() == relative
    assert result.datetime_relative() == result._now + relative
    precise = precise_conversion(
        result, second, minute, hour, day, week, month, year, decade, century
    )
    assert result.datetime_precise() == precise
    assert result.timedelta_precise() == precise - result._now


def test_invalid_unit():
    with pytest.raises(ValueError):
        IntervalConverter("", max_unit="invalid")  # type: ignore
