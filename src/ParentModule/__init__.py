print(" ParentModule.__init__.py loaded ")


class Parent:
    def __init__(self, message):
        self.message = message
        self.run()

    def printMessage(self):
        print(f" | Parent | {self.message}")
