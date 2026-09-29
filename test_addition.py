from addition import no_addition

def test_positive_no():
    assert no_addition(10,40)== 40

def test_zero():
    assert no_addition(10,0)== 10

def test_negative():
    assert no_addition(-10,20)==10   