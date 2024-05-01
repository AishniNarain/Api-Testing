import unittest

from unittest.mock import patch, call
from mocking.sample2 import random_sum

@patch("mocking.sample2.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3,4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls = [call(1,10),call(1,7)])