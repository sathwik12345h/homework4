import pytest
from faker import Faker
import random

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=0, type=int, help="Number of random test records")

@pytest.fixture(scope='session')
def num_records(request):
    """Fixture to get the number of records from the command line."""
    return request.config.getoption("--num_records")

@pytest.fixture(params=[()])
def random_test_data(request, num_records):
    """Fixture to generate random test data based on num_records."""
    if not hasattr(request, 'param_index'):
        request.param_index = 0

    if request.param_index >= num_records:
        pytest.skip("Skipping test as num_records limit reached.")

    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    operation = random.choice(["add", "subtract", "multiply", "divide"])

    if operation == "divide" and b == 0:
        b = 1  # Avoid division by zero

    request.param_index += 1
    return a, b, operation
