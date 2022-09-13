import datetime
import random

import pytest

import time_str

test = (
    random.randrange(0, 61),
    random.randrange(0, 61),
    random.randrange(0, 25),
    random.randrange(0, 366),
    random.randrange(0, 5),
    random.randrange(0, 13),
    random.randrange(0, 100),
    random.randrange(0, 100),
    random.randrange(0, 10),
)
tests = [test for _ in range(1000)]


@pytest.fixture
def converter():
    """Returns a converter."""
    return time_str.convert


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
        + round(30.5 * month)
        + (365 * year)
        + 7 * week
        + 3650 * decade
        + 36500 * century,
    )
