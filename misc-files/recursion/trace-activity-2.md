### Tracing Recursive Code
Consider the following code:

```

def mystery(n):
    return mystery_helper([], n)

def mystery_helper_helper(prev):
    if len(prev) < 2:
        return []
    else:
        return [prev[0] + prev[1]] + mystery_helper_helper(prev[1:])

def mystery_helper(lst, i):
    if i == 0:
        lst.append([1])
    else:
        mystery_helper(lst, i-1)
        print(lst[-1])
        lst.append([1] + mystery_helper_helper(lst[i-1]) + [1])

mystery(6)

```

### Output
What is the output of this code?

<br><br><br><br><br><br><br><br><br><br>

### Recursive Call Graph
Draw the graph of the recursive calls for each call to `mystery_helper`

<br><br><br><br><br><br><br><br><br><br><br><br>


### Recursive Call Graph
Each call to `mystery_helper` calls `mystery_helper_helper` which is also recursive.
Draw the graph of the recursive calls for `mystery_helper_helper` for a couple of the
calls to `mystery_helper`.

<br><br><br><br><br>


