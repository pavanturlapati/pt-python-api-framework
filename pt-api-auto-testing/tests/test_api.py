import pytest
import requests
from utils.data_loader import load_json

test_data = load_json('test_data/test_data.json')

@pytest.mark.parametrize("data", test_data)
def test_api(data):
    response = requests.request(
        method=data['method'],
        url=data['endpoint'],
        headers=data.get('headers', {}),
        json=data.get('body', {})
    )
    
    assert response.status_code == data['expected_status'], f"Expected {data['expected_status']} but got {response.status_code}"

    # Optionally, you can add more assertions for response body, headers, etc.
