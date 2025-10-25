from main import get_weather, add, divide, UserManager, is_prime

import pytest, requests

def test_get_weather():
    assert get_weather(30) == "hot"
    assert get_weather(21) == "cold"


def test_add():
    assert add(2,3) == 5, "2 + 3 should be 5"
    assert add(-1,1) == 0, "-1 + 1 should be 0"
    assert add(0,0) == 0, "0 + 0 should be 0"


def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10,0)


@pytest.fixture
def user_manager():
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")


@pytest.mark.parametrize("num, expected", [
    (1, False),
    (3, True),
    (17, True),
    (19, True),
    (25, False),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected


def test_get_weather(mocker):
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    result = get_weather("Dubai")

    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
