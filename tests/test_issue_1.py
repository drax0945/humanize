"""Tests for issue #1: ordinal() returns wrong suffix for 11, 12, 13."""

from humanize import number


class TestOrdinalTeens:
    """ordinal() should return "th" for 11, 12 and 13 (and teens in hundreds)."""

    def test_eleven(self) -> None:
        assert number.ordinal(11) == "11th"

    def test_twelve(self) -> None:
        assert number.ordinal(12) == "12th"

    def test_thirteen(self) -> None:
        assert number.ordinal(13) == "13th"

    def test_twenty_two(self) -> None:
        assert number.ordinal(22) == "22nd"

    def test_teens_in_hundreds(self) -> None:
        assert number.ordinal(112) == "112th"

    def test_hundred_twelve(self) -> None:
        assert number.ordinal(212) == "212th"
