# Example of a parent class calling a child class method on initialization
print(" ParentChildSingleFile.py | loaded ")


class Parent:
    def __init__(self, message):
        self.message = message
        self.run()

    def printMessage(self):
        print(f" | Parent | {self.message}")


class Child(Parent):
    def run(self):
        """ called from the __init__ of the parent class """
        print(" | Child  | run()")
        self.printMessage()


# allow for command-line execution
if __name__ == '__main__':
    Child(message="Hello from Command-Line")
