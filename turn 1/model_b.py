import pytest
from my_decision_system import make_decision

# Sample data for testing
test_data = [
    ({"input_1": 10, "input_2": 20}, "Accept"),
    ({"input_1": 5, "input_2": 15}, "Reject"),
    ({"input_1": 15, "input_2": 10}, "Review"),
]

@pytest.mark.parametrize("input_data, expected_outcome", test_data)
def test_make_decision(input_data, expected_outcome):
    """
    Test the make_decision function with different input scenarios.
    """
    actual_outcome = make_decision(input_data)
    assert actual_outcome == expected_outcome, f"Expected {expected_outcome}, but got {actual_outcome}"

if __name__ == "__main__":
    pytest.main()
