# Example of a parent class calling a child class method on initialization

from ParentModule.Parent import Parent

print(" ParentChildModules | loaded ")

class Child(Parent):
    def run(self):
        """ called from the __init__ of the parent class """
        print(f" | Child  | run()")
        self.printMessage()

# allow for command-line execution: `python MyApp.py option=value`
if __name__ == '__main__':
    Child(message="Hello!")
