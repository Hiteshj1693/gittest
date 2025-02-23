class A:
    def __init__(self):
        pass
    def prtA(self):
        print("A")
class B(A):
    def __init__(self):
        pass
    def prtB(self):
        print("B")
class C(B):
    def __init__(self):
        super().__init__()
    def prtC(self):
        print("C")

c=C()
c.prtA()