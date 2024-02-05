# Tracing References in Code

Consider the following code:

```
class Car:

    def __init__(self, color, doors):
        self.color = color
        self.doors = doors
    
    def get_doors(self):
        return self.doors
    
    def set_doors(self, d):
        self.doors = d;
    
    def repaint(self, c):
        self.color = c
    
    def get_color(self):
        return self.color
    
    def crash(self, c2, c3):
        c4 = c3;
        c5 = Car("orange", 2)
        c3 = c5
        self.repaint(c2.get_color())
        self.doors -= 1
        c4.set_doors(c4.get_doors()-2)
        c2 = self
        c3.repaint(self.color)
        c5.repaint("blue")
        c2 = c5
    
if __name__ == '__main__':
    c1 = Car("black", 4)
    c2 = Car("yellow", 3)
    c3 = Car("green", 2)

    c3.crash(c1,c2)
        
    print(c1.get_color())
    print(c2.get_color())
    print(c3.get_color())

    print(c1.get_doors())
    print(c2.get_doors())
    print(c3.get_doors())

    c4 = Car("black", 4)
    c5= Car("green", 2)

    c4.crash(c5,c5)
    print(c4.get_color())
    print(c5.get_color())
    print(c4.get_doors())
    print(c5.get_doors())
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

