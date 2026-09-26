"""Ordinal number tests."""

from __future__ import annotations

import pytest

import humanize


@pytest.mark.parametrize(
    "value, expected",
    [
        (11, "11th"),
        (12, "12th"),
        (13, "13th"),
        (111, "111th"),
        (112, "112th"),
        (113, "113th"),
        (121, "121st"),
        (-11, "-11th"),
        (-12, "-12th"),
        (-13, "-13th"),
        (-21, "-21st"),
    ],
)
def test_ordinal_teen_suffixes(value: int, expected: str) -> None:
    assert humanize.ordinal(value) == expected
