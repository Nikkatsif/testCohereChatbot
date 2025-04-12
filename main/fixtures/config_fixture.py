import json
import pytest

@pytest.fixture
def config():
    """Load configuration from config.json."""
    with open('config/config.json', 'r') as file:
        return json.load(file)