from typing import Callable, Union

class if_:
    def __init__(self, condition: bool):
        self.condition = condition
        self.done = False
    def do(self, action: Callable):
        if self.condition:
            self.done = True
            action()
        return self

class elif_:
    def __init__(self, parent: Union[if_, 'elif_'], condition: bool):
        self.parent = parent
        self.condition = condition
    def do(self, action: Callable):
        if self.condition and not self.parent.done:
            self.parent.done = True
            action()
class else_:
    def __init__(self, parent: if_):
        self.parent = parent
    def do(self, action: Callable):
        if not self.parent.done:
            self.parent.done = True
            action()
if __name__ == '__main__':
    from random import randint
    i = randint(0, 15)
    a = if_(i<3).do(lambda: print("if st"))
    elif_(a, i<7).do(lambda: print("elif 1"))
    elif_(a, i>7).do(lambda: print("elif 2"))
    elif_(a, i==7).do(lambda: print("elif 3"))
    else_(a).do(lambda: print("else"))
