from app.main import get_coin_combination



def test_base_cases():
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_single_coin_cases():
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]

def test_multiple_coin_cases():
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(97) == [2, 1, 1, 3]

def test_edge_cases():
    assert get_coin_combination(98) == [3, 1, 1, 3]
