import pytest

from availability import calculate_availability


def test_availability_with_20_minutes_downtime():
    result = calculate_availability(43200, 20)
    assert result == 99.954


def test_full_availability():
    result = calculate_availability(43200, 0)
    assert result == 100.000


def test_negative_downtime():
    with pytest.raises(ValueError):
        calculate_availability(43200, -10)


def test_downtime_cannot_exceed_total_time():
    with pytest.raises(ValueError):
        calculate_availability(100, 120)
