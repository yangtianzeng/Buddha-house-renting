from django.test import TestCase

# Create your tests here.
a = 0
def test():

    global a
    a = 123

def testa():
    print(a)

test()
print(a)
testa()