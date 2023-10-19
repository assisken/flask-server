from mock import Mock, patch
from server.repository import User, Users


def add_arg(a, b, printer=print):
    printer("запускаю сложение 💣💣💣")
    return a + b


def test_mock_as_argument():
    mock = Mock()
    
    assert 3 == add_arg(1, 2, mock)
    mock.assert_called_with("запускаю сложение 💣💣💣")







def add(a, b):
    print("запускаю сложение 💣💣💣")
    return a + b


@patch('builtins.print')
def test_mock_as_decorator(mock):
    assert 3 == add(1, 2)
    mock.assert_called_with("запускаю сложение 💣💣💣")


def test_mock_as_context_manager():
    with patch('builtins.print') as mock:
        assert 3 == add(1, 2)
    mock.assert_called_with("запускаю сложение 💣💣💣")



def some_db_request(repository: Users):
    result = repository.get_one(1)
    return result


def test_mock_as_object():
    oleg = User(id=1, first_name="Oleg", middle_name="Oof", surname="")

    mock = Mock()
    mock.get_one.return_value = oleg

    assert some_db_request(mock) == oleg
    mock.get_one.assert_called_with(1)
