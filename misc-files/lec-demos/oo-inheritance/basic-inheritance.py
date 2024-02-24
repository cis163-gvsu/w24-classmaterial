from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    def move(self, xchange, ychange):
        self.x += xchange
        self.y += ychange

    @abstractmethod
    def make_noise(self):
        pass

    def __str__(self):
        return f'animal named {self._name}'

class Fish(Animal):
    def __init__(self, name):
        self.x = 0
        self.y = 0
        super().__init__(name)
        
    def make_noise(self):
        print('blub blub')

class Dog(Animal):
    def __init__(self, name, weight):
        self.weight = weight
        super().__init__(name)

    def make_noise(self):
        noise = ''
        for i in range(self.weigth//10):
             noise += 'woof'
        print(noise)

if __name__ == '__main__':
    #anim = Animal("Fred")
    #print(anim)
    flounder = Fish('flounder')
    print(flounder._name)
    print(flounder)
