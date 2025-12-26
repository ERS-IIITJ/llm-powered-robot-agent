# Test file for example_function in functions/example.py
#run 'pytest tests/test_example.py' to execute these tests

from functions.example import example_function


def test_example_function_returns_string():
    result = example_function()
    assert isinstance(result, str)


def test_example_function_value():
    result = example_function()
    assert result == "hello"
