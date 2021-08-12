# python-if_statements
support for control flow in python

There are two main ways to implement If/Elif/Else statements in python:

1.Using a variable:

a. Initialize an instance of If, bind it to a variable, and give it a condition as well as an action (which is a function, followed by any number of arguments).
<pre>
    <code>
    Basic instantiation:
        my_if = If(i == 0)
        my_if.do(print, "i is 0", F"{i = }")
    
    One liner:
        my_if = If(i == 0).do(print, "i is 0", F"{i = }")
    
    For clarity:
        my_if = If(i == 0).do(
            print, "i is 0", F"{i = }"
            )
    </code>
</pre>  
b. Attach any number of Elif instances to it, and a single instace of Else. Remember that Else does not have any conditions.
<pre>
    <code>
    Elif(my_if, i == 1).do(
        print, "i is 1", F"{i = }"
    )
    Elif(my_if, i == 2).do(
        print, "i is 2", F"{i = }"
    )
    Else(my_if).do(
        print, "i is not 0, 1, or 2", F"{i = }"
    )
    </code>
</pre>



2.Chaining method access:

a.In this case, it's really easy to instantiate If. Initialization and declaration of all of its Elif objecs and its instance of Else are done in a single command.
There's also no need to bind your instance of If to a variable, nor to pass it to its subsequent children.

The same example from the first method would be written like this:

<pre>
    <code>
    If(i == 0).do(
        print, "i is 0", F"{i = }"
    ).Elif(i == 1).do(
        print, "i is 1", F"{i = }"
    ).Elif(i == 2).do(
        print, "i is 2", F"{i = }"
    ).Else().do(
        print, "i is not 0, 1, or 2", F"{i = }"
    )
    </code>
</pre>

You can also make the code clearer by inserting a line break after the conditional instantiation.

<pre>
    <code>
    If(i == 0
        ).do(
        print, "i is 0", F"{i = }"
    ).Elif(i == 1
        ).do(
        print, "i is 1", F"{i = }"
    ).Elif(i == 2
        ).do(
        print, "i is 2", F"{i = }"
    ).Else(
        ).do(
        print, "i is not 0, 1, or 2", F"{i = }"
    )
    </code>
</pre>
