import pytest

def test_fun(num3,num2):

    return num3 + num2
class Testdomo1(object):
    def test_med(self):
        result=test_fun(1,2)
        assert 3==result
        print("11")
if __name__ == '__main__':
    pytest.main(['-s', 'html_pytest.py'])