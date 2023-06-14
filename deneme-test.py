from deneme import Add

def TestAdd():
    assert Add(2,3) == 5
    assert Add(27,3) == 6
    print("add function works correctly")
    
if __name__ == '__main__':
    TestAdd()