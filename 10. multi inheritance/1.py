class A:
    def do_this(self):
        print("Doing this in A")

class B(A):
    pass

class C:
    def do_this(self):
        print("Doing this in C")

class D(B, C):
    pass

print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]