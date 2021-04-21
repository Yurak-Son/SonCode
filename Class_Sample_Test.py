class A:
    def __init__(self):
        self._name = ''

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

a = A()
a.name = "12"

a_list = []

a_list.append(a)

print(a)
