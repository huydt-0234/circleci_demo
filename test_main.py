from tkinter import N
from main import hello, add

def test_add():
    assert add(2, 3) == 5, "should be 5"
    print("Correctly")
    assert Add(5,5) == 11

def test_hello():
    assert hello("huy") == "Hello_huy", "should be Hello huy" 

if __name__=="__main__":
    test_add()
