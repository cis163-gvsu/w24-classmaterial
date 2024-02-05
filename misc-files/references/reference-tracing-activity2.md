# Tracing References in Code
Consider the following code:

```
class Misc:

    def __init__(self, color, name, num):
        self.color = color
        self.num = num
        self.name = name
        self.lst = [ord(name[i]) for i in range(len(name))]
            
    def mystery(self, first, second):
        third = second
        first.name = third.name
        first.num = self.num
        fourth = Misc('lime', 'Maxwell', 8)
        first.num -= 1
        second.num += 2
        second.lst[-1] = 'z'
        second = fourth
        fourth.lst[-1] = 'a'
        fourth.name = fourth.name.upper()
        third.name.lower()
        first.color = self.color
        second.color = third.color
        fourth.num += 10
        third.name = 'foobar'
        return self, fourth
    
def foo(m1, m2, x1, x2):
    temp = m1.num
    m1.num = temp
    x1 = temp
    return x1 + m1.num + m2.num + x2
    
if __name__ == '__main__':
    A = Misc('cyan', 'Inky', 80)
    B = Misc('red', 'Blinky', 29)
    C = Misc('orange', 'Cylde', 14)
    D = Misc('black', 'Spunky', 18)
    E = Misc('pink', 'Pinky', 47)
    F = Misc('green', 'Funky', 76)

    F, Y = D.mystery(A,C)
    
    print(f'{A.color}, {A.name}, {A.num}')
    print(f'{D.color}, {D.name}, {D.num}')
    print(f'{C.color}, {C.name}, {C.num}')
    print(f'{F.color}, {F.name}, {F.num}')
    print(f'{Y.color}, {Y.name}, {Y.num}')

    x1 = 3
    x2 = 4

    x2 = foo(D, E, x2, x1)

    print(D.num)
    print(E.num)

    W, Z = E.mystery(B,B)
    print(f'{B.color}, {B.name}, {B.num}')
    print(f'{E.color}, {E.name}, {E.num}')
    print(f'{W.color}, {W.name}, {W.num}')
    print(f'{Z.color}, {Z.name}, {Z.num}')
```

What is the output of this code?

Line 1:

Line 2:

Line 3:

Line 4:

Line 5:

Line 6:

Line 7:

Line 8:

Line 9:

Line 10:

Line 11:
