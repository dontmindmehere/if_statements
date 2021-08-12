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



    def Elif(self, *condition: bool):
        return Elif(self, *condition)
    def Else(self, *condition: bool):
        return Else(self, *condition)


class Elif:
    def __init__(self, parent: Union[If, 'Elif'], condition: bool):
        self.parent = parent
        self.condition = condition

    def do(self, action: Callable, *args: Any):
        if self.condition and not self.parent.done:
            self.parent.done = True
            action(*args)
        return self.parent


class Else:
    def __init__(self, parent: If):
        self.parent = parent

    def do(self, action: Callable, *args: Any):
        if not self.parent.done:
            self.parent.done = True
            action(*args)
        return self.parent


if __name__ == '__main__':
    """There are various ways to use If/Elif/Else:
    """

    for i in range(5):
        """Using a variable and a one line
        for each condition and action
        """
        a = If(i == 0).do(print, "If\t", F"{i = }")
        Elif(a, i == 1).do(print, "Elif\t", F"{i = }")
        Elif(a, i == 2).do(print, "Elif\t", F"{i = }")
        Elif(a, i == 3).do(print, "Elif\t", F"{i = }")
        Else(a).do(print, "Else\t", F"{i = }")


    for i in range(5):
        """Using a variable and line breaks for clarity
        """
        a = If(i == 0).do(
            print, "If\t", F"{i = }"
        )
        Elif(a, i == 1).do(
            print, "Elif\t", F"{i = }"
        )
        Elif(a, i == 2).do(
            print, "Elif\t", F"{i = }"
        )
        Elif(a, i == 3).do(
            print, "Elif\t", F"{i = }"
        )
        Else(a).do(
            print, "Else\t", F"{i = }"
        )

    for i in range(5):
        """Chaining method access, to save space
        while maintaining some clarity
        """
        If(i == 0).do(
            print, "If\t", F"{i = }"
        ).Elif(i == 1).do(
            print, "Elif\t", F"{i = }"
        ).Elif(i == 2).do(
            print, "Elif\t", F"{i = }"
        ).Elif(i == 3).do(
            print, "Elif\t", F"{i = }"
        ).Else().do(
            print, "Else\t", F"{i = }"
        )

    """
    # TODO:
    --loops
        -while loops --> While(condition).do(action)
        -for loops --> For(initial action, condition, action at end of loop)
        -foreach loops -> ForEach(iterable).do(action)
    --support for break in loops
    --suport for Else statements after loops
    """
