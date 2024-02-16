### Tracing Recursive Code
Consider the following code:

```
class Mystery:

    def __init__(self):
        self.val = 0

    def foo(self, s):
        self. val += 1
        if len(s) == 1:
            return s;

        res1 = self.foo(s[:len(s)//2])
        res2 = self.foo(s[len(s)//2:])
        if res1[-1] == res2[0]:
            return res1 + res2[1:]
        else:
            return res1 + res2


m = Mystery()
print(m.foo("abcde"))
print(m.val)
print(m.foo("aabcbba"))
print(m.val)
print(m.foo("aaabbbccdeff"))
print(m.val)
```

### Output
What is the output of this code?

Line 1:


Line 2:


Line 3:


Line 4:


Line 5:


Line 6:


### Recursive Call Graph
Draw the graph of the recursive function calls for
each call to `foo` above.




