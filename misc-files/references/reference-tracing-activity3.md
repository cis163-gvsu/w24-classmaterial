# Tracing References in Code

Consider the following code:

```
class Weird:
    def __init__(self, name, a, b, vals):
        self.name = name.lower()
        self.state = {'a': a, 'b': b, 'vals': vals}
        which = 1

    def swap(self):
        if which == 1:
            self.name = self.name.upper()
        else:
            self.name = self.name.lower()
    
    def __str__(self):
        out = f"name = {self.name}, a = {self.state['a']}, b = {self.state['b']}"
        out += f", vals = {self.state['vals']}"
        return out

class Strange:
    def __init__(self, things, label):
        self.things = things
        self.label = label
            
    def do_stuff(self, other):
        temp1 = other.things[2]
        d1 = temp1.state
        temp2 = self.things[2]
        d2 = temp2.state
        d1['b'] += 20
        other.things[2] = temp2
        self.things[2] = temp1
        temp1.state = d2
        d2['a'] -= 20

    def __str__(self):
        out = f'Strange {self.label}\n'
        for thing in self.things:
            out += f'\t{thing}\n'
        return out

if __name__ == '__main__':
    w1 = Weird('cat', 105, 101, [8,19,2,5,7])
    w2 = Weird('dog', 106, 102, [2,55,88,16,68])
    w3 = Weird('narwhal', 107, 103, [11,13,82,83,49])
    w4 = Weird('sea serpent', 108, 104, [7,9,52,78,67])
    w5 = Weird('clownfish', 109, 119, [24,13,81,79,66])
    w6 = Weird('starfish', 110, 120, [98,3,14,16,7])
    w7 = Weird('unicorn', 113, 114, [17,19,42,68,57])
    w8 = Weird('hippogriff', 115, 118, [27,29,22,28,27])

    s1 = Strange([w1,w2,w3], 'land')
    s2 = Strange([w3,w4,w5], 'sea')
    s3 = Strange([w4,w7,w8], 'mythical')

    # Part A Output
    print(s1)
    print(s2)
    print(s3)
    print('-----end part A output-----\n')

    s1.do_stuff(s2)
    # Part B Output
    print(s1)
    print(s2)
    print(s3)
    print('-----end part B output-----\n')

    temp = w2
    w2 = w1
    w1 = w3
    w3 = temp
    # Part C Output
    print(s1)
    print(s2)
    print(s3)
    print('-----end part C output-----\n')

    s3.do_stuff(s2)
    s2.do_stuff(s1)
    # Part D Output
    print(s1)
    print(s2)
    print(s3)
    print('-----end part D output-----\n')

    s1.things[-1] = w4
    s1.things[0] = w8
    s1.do_stuff(s1)
    # Part E Output
    print(s1)
    print(s2)
    print(s3)
    print('-----end part E output-----\n')
```

## What is the output for part A?
<br><br><br><br><br><br>

## What is the output for part B?
<br><br><br><br><br><br>


## What is the output for part C?
<br><br><br><br><br><br>


## What is the output for part D?
<br><br><br><br><br><br>


## What is the output for part E?
<br><br><br><br><br><br>


