import pytest
from lib.password_checker import PasswordChecker

def test_for_valid():
    checker = PasswordChecker()
    assert checker.check('12345678') == True
    assert checker.check('abcdefghijklmnopqrstuvwxyz') == True
    assert checker.check('ralm30f8') == True
    assert checker.check('0000000000') == True

def test_for_short_string():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check('1234')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

