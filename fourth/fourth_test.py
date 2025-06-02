from fourth.fourth import calculator, read_yaml
import pytest

from contextlib import nullcontext

@pytest.mark.parametrize(
    "y, x, operation, exception, want",
    [
        (1, 3, "addition", nullcontext(), 4),
        (1, 3, "subtraction", nullcontext(), -2),
        (1, 3, "multiplication", nullcontext(), 3),
    ]
)
def test_calculator(y, x, operation, exception, want):
    with exception:
        assert calculator(y, x, operation) == want

@pytest.mark.parametrize(
    "filepath, exception, want",
    [
        ("mybadpath", pytest.raises(ValueError), None),
    ]
)
def test_read_yaml(filepath, exception, want):
    with exception:
        assert read_yaml(filepath) == want

