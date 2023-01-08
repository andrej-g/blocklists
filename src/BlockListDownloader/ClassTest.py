from Templates import Templates


class ClassTest:
    def __init__(self, parameter1: str, dictionary1: dict, template: type[Templates], list1: list[str]):
        self.parameter1 = parameter1
        self.dictionary1 = dictionary1
        self.template = template
        self.list1 = list1

    @staticmethod
    def foo(self):
        foo1: str

        if self.parameter1 == "test":
            foo1 = "asdf"
        else:
            foo1 = "fdsa"

        foo2 = self.dictionary1
        foo3 = self.template
        foo4 = self.list1
