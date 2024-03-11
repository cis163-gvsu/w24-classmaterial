# Tracing References in Code

Consider the following code:

```
class Car:

    def __init__(self, color, doors, passengers):
        self.color = color
        self.__doors = doors
        self.passengers = passengers
    
    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, ndoors):
        self.__doors = ndoors

    def repaint(self, c):
        self.color = c
    
    def crash(self, c2, c3):
        c4 = c3;
        c4.doors -= 1
        c5 = Car("orange", 2, c3.passengers)
        c2.repaint(self.color)
        self.repaint(c4.color)
        c3.doors -= 1
        c3.passengers.pop()
        c2.passengers.pop()
        c2 = self
        c2.repaint(self.color)
        self.passengers = c3.passengers
        c5.repaint("purple")
        c5.passengers.pop()
        c6 = c4
        c6.doors -= 1
        return c5
    
if __name__ == '__main__':
    c1 = Car("silver", 2, ["bob", "anne", "fred"])
    c2 = Car("yellow", 4, ["chuck", "freddy", "tina"])
    c3 = Car("blue", 3, ["ted", "tom", "tracy"])

    c4 = c2.crash(c3,c1)
        
    print(c1.color)
    print(c1.doors)
    print(c1.passengers)

    print(c2.color)
    print(c2.doors)
    print(c2.passengers)
    
    print(c3.color)
    print(c3.doors)
    print(c3.passengers)
    
    print(c4.color)
    print(c4.doors)
    print(c4.passengers)

```

## Part 1:  What is the output of this code?

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

Line 12:


## Part 2:  Changing the Setter
What if we changed the setter for the property `doors` to be:
```
    @doors.setter
    def doors(self, ndoors):
        if ndoors >= 0:
            self.__doors = ndoors
```

Would this change the output?  If so, how many lines change and what do they change to?
