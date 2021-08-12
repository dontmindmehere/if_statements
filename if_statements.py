from typing import Callable, Union, Any

class If:
    def __init__(self, condition: bool):
        self.condition = condition
        self.done = False

    def do(self, action: Callable, *args: Any):
        if self.condition:
            self.done = True
            action(*args)
        return self


class Elif:
    def __init__(self, parent: Union[If, 'Elif'], condition: bool):
        self.parent = parent
        self.condition = condition

    def do(self, action: Callable, *args: Any):
        if self.condition and not self.parent.done:
            self.parent.done = True
            action(*args)


class Else:
    def __init__(self, parent: If):
        self.parent = parent

    def do(self, action: Callable, *args: Any):
        if not self.parent.done:
            self.parent.done = True
            action(*args)



if __name__ == '__main__':
    for i in range(5):
        a = If(i == 0).do(print, "If\t", F"{i = }")
        Elif(a, i == 1).do(print, "Elif\t", F"{i = }")
        Elif(a, i == 2).do(print, "Elif\t", F"{i = }")
        Elif(a, i == 3).do(print, "Elif\t", F"{i = }")
        Else(a).do(print, "Else\t", F"{i = }")
