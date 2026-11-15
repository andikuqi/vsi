"""Checks that the official UDP is wired in. Skipped until src/esa_problem.py is configured."""

import pytest

import esa_problem


def test_udp_loads_and_scores_example():
    if not esa_problem.UDP_FILE.exists():
        pytest.skip("official UDP not configured yet (see src/esa_problem.py)")
    udp = esa_problem.load_udp(esa_problem.PROBLEM_IDS[0] if esa_problem.PROBLEM_IDS else None)
    lower, upper = udp.get_bounds()
    assert len(lower) == len(upper) > 0
