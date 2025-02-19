import pytest
from main import main


@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["5", "3", "add", "n"], "The result of 5.0 add 3.0 is equal to 8.0"),
        (["10", "2", "subtract", "n"], "The result of 10.0 subtract 2.0 is equal to 8.0"),
        (["4", "5", "multiply", "n"], "The result of 4.0 multiply 5.0 is equal to 20.0"),
        (["20", "4", "divide", "n"], "The result of 20.0 divide 4.0 is equal to 5.0"),
        (["1", "0", "divide", "n"], "An error occurred: Cannot divide by zero."),
        (["9", "3", "unknown", "n", "n"], "Unknown operation: unknown"),
        (["a", "3", "add", "n"], "Invalid number input: a or 3 is not a valid number."),
        (["5", "b", "subtract", "n"], "Invalid number input: 5 or b is not a valid number."),
    ],
)
def test_main(capsys, monkeypatch, inputs, expected_output):
    # We ensure that there's always an "n" for the exit prompt.
    if inputs[-1].lower() != "n":
        inputs.append("n")

    def mock_input(_):
        return inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    main()

    captured = capsys.readouterr()
    assert expected_output in captured.out
