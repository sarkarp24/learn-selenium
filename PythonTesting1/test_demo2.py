import pytest

def test_demoFuncTwo():
    print("Hello")

@pytest.mark.skip
def test_creditCardBalance():
    balance = 1000
    print('creditCardBalanace function')
    assert balance == 1000

