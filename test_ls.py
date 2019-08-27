#list of num and key exists ==>True

#list of numm and key doesnt not exit

#if list is empty =>

# if key is noe


from linear_search import linear_search
import pytest


@pytest.mark.valid
def test_valid_pos_input():
    result = linear_search(1000,50)

    assert result == True



def test_valid_neg_input():
    result = linear_search(1000,5120)
    assert result == False

@pytest.mark.valid    
def test_invalid_input():
    result = linear_search(0,0)
   # assert result == False
