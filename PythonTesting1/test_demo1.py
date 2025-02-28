import pytest

def test_demoFuncOne():
    print("Hello")

@pytest.mark.smoke
def test_creditCard():
    card = 'Credit Card'

    assert card == 'Dabit Card'

