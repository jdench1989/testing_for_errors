import pytest
from lib.present import Present

def test_present_wrap():
    present = Present()
    present.wrap('A gift')
    assert present.contents == 'A gift'

def test_present_unwrap():
    present = Present()
    present.wrap('A gift')
    result = present.unwrap()
    assert result == 'A gift'

def test_present_already_wrapped_error():
    present = Present()
    present.wrap('A gift')
    with pytest.raises(Exception) as e:
        present.wrap('Another gift')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_present_nothing_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."