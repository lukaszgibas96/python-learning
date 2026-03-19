from um import count

def test_count_1():
    assert count("Um, how are um, you?") == 2

def test_count_2():
    assert count("The album is cool um... What do you think?") == 1

def test_count_3():
    assert count("Um, thanks, um...") == 2
