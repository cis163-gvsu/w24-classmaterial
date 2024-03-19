# Tracing Exceptions - Wednesday

Consider the following code:

```
class ExceptionFun:
  
    def __init__(self, n):
        self.mylst = []
        for i in range(n):
            self.mylst = None

    def mixup(self):
        for i in range(1, len(self.mylst)+1):
            self.mylst[i].repaint(i)

class Car:
    def __init__(self):
        self.color = 'blue'
        self.doors = 4

    def repaint(self, num):
        if num % 3 == 0:
            self.color = 'black'
        elif num % 2 == 0:
            self.color = 'silver'
        else:
            self.color = 'white'


if __name__ == '__main__':
    ef = ExceptionFun(10)
    try:
        print('calling mixup')
        ef.mixup()
        print('done calling mixup')
    except IndexError:
        print('tried to access out of bounds')
    except Exception:
        print('other exception')
    finally:
        print('all finished')

```

What is the output of this code?



