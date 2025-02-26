import pytest
from main import main

@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["add", "5", "3", "exit"], "The result of 5.0 add 3.0 is 8.0"),
        (["subtract", "10", "2", "exit"], "The result of 10.0 subtract 2.0 is 8.0"),
        (["multiply", "4", "5", "exit"], "The result of 4.0 multiply 5.0 is 20.0"),
        (["divide", "20", "4", "exit"], "The result of 20.0 divide 4.0 is 5.0"),
        (["divide", "1", "0", "exit"], "Error: Cannot divide by zero."),
        (["unknown", "exit"], "Invalid input. Please enter valid numbers."),  # Updated to match main.py
        (["a", "3", "add", "exit"], "Invalid input. Please enter valid numbers."),
        (["5", "b", "subtract", "exit"], "Invalid input. Please enter valid numbers."),
    ],
)
def test_main(capsys, monkeypatch, inputs, expected_output):
    """
    Tests the main calculator CLI by simulating user inputs and verifying expected output.
    """
    inputs_iter = iter(inputs + ["exit"])  # Ensure "exit" is always included

    def mock_input(_):
        try:
            return next(inputs_iter)
        except StopIteration:
            pytest.fail("Test ran out of input values!")

    monkeypatch.setattr("builtins.input", mock_input)

    main()

    captured = capsys.readouterr()
    assert expected_output in captured.out
