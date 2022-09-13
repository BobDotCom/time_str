import datetime
import random

import pytest

import time_str

maxes = (
    62,
    62,
    25,
    366,
    5,
    14,
    100,
    100,
    10,
)


def make_value() -> tuple[int, int, int, int, int, int, int, int, int]:
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


@pytest.fixture
def converter():
    """Returns a converter."""
    return time_str.convert_str


@pytest.mark.parametrize("second,minute,hour,day,week,month,year,decade,century", tests)
def test_conversions(
    converter, second, minute, hour, day, week, month, year, decade, century
):
    assert converter(
        f"{second} {random.choice(['seconds', 'second', 'secs', 'sec', 's'])} "
        f"{minute} {random.choice(['minutes', 'minute', 'mins', 'min', 'm'])} "
        f"{hour} {random.choice(['hours', 'hour', 'hrs', 'hr', 'h'])} "
        f"{day} {random.choice(['days', 'day', 'dys', 'dy', 'd'])} "
        f"{week} {random.choice(['weeks', 'week', 'wks', 'wk', 'w'])} "
        f"{month} {random.choice(['months', 'month', 'mons', 'mon', 'mn'])} "
        f"{year} {random.choice(['years', 'year', 'yrs', 'yr', 'y'])} "
        f"{decade} {random.choice(['decade', 'decades', 'dcd', 'dec'])} "
        f"{century} {random.choice(['century', 'centuries', 'c', 'cen'])}"
    ) == datetime.timedelta(
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


def test_deprecated():
    with pytest.warns(DeprecationWarning):
        assert time_str.convert("1 second") == time_str.convert_str("1 second")
