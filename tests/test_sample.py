from unittest.mock import Mock, patch

# from mocking.sample import guess_number
from mocking.sample import get_ip

# @mock.patch("mocking.sample.roll_dice")
# def test_guess_number1(mock_roll_dice):
#     mock_roll_dice.return_value = 3
#     assert guess_number(3) == "You Won!"
#     mock_roll_dice.assert_called_once()

# #Parameterizing functions
# @pytest.mark.parametrize("input_value, expected_value", [(3,"You Won!"),(4,"You lost!")])
# @mock.patch("mocking.sample.roll_dice")
# def test_guess_number2(mock_roll_dice,input_value, expected_value):
#     mock_roll_dice.return_value = 3
#     assert guess_number(input_value) == expected_value

@patch("mocking.sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_response = Mock(status_code =200)
    mock_response.json.return_value= {"origin":"0.0.0.0"}
    
    mock_requests_get.return_value = mock_response
    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")
    
