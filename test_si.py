from sim_interest import simple_interest

def test_invalid principal():
    assert simple_interest(-28000,2,3)== 13

def test_invalid time():
    assert simple_interest(10000,-9,4)== 30

def test_invalid rate():
    assert simple_interest(10000,2,-3)== 39 
    
     