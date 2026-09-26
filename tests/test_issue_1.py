import pytest

import humanize


class TestOrdinalIssue1:
    """Regression tests for gh#1: ordinal(12) returns '12nd' instead of '12th'."""

    def test_ticket_12(self):
        """Ticket example: ordinal(12) should be '12th'."""
        assert humanize.ordinal(12) == "12th"

    def test_11(self):
        """11 should be '11th'."""
        assert humanize.ordinal(11) == "11th"

    def test_13(self):
        """13 should be '13th'."""
        assert humanize.ordinal(13) == "13th"

    def test_22(self):
        """22 should be '22nd' (not affected by the teen rule)."""
        assert humanize.ordinal(22) == "22nd"

    def test_112(self):
        """112 (teens inside hundreds) should be '112th'."""
        assert humanize.ordinal(112) == "112th"
