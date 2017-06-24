class Square(object):
    def __init__(self, length,name):
        self._length = length
        self._name = name
    def display(self):
        print("length : ", self.length
              )
        print("Name : ", self.name
              )
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def names(self):
     return self._name

    @names.setter
    def name(self, value):
        self._name = value



r = Square(9,"Krishna")
r.length  # automatically calls getter
r.display()
r.length = 12  # automatically calls setter
r.name= "Bhanu"
r.display()