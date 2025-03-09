def greet(name):
    def say_hi():
        print("Say Hi before execution!")
        name()
        print("Say Hi after execution!")

    return say_hi


@greet
def hey():
    print("Hey executed!")

hey()
