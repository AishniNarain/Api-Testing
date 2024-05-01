from unittest.mock import Mock,patch, call
from mocking.sample2 import random_sum, silly_func

@patch("mocking.sample2.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3,4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls = [call(1,10),call(1,7)])

@patch("mocking.sample2.time.time")
@patch("mocking.sample2.random.randint")
@patch("mocking.sample2.requests.get")
def test_silly_func(mock_requests_get, mock_randint, mock_time):
    test_params = {
        "timestamp": 123,
        "number" : 5
    }
    
    mock_time.return_value = test_params['timestamp']
    mock_randint.return_value = test_params['number']
    
    mock_response = Mock(status_code = 200)
    mock_response.json.return_value = {"args":test_params}
    
    mock_requests_get.return_value = mock_response
    
    assert silly_func() == test_params
    
    