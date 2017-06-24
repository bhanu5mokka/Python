import self as self


class Personal:
    
    def __init__(self, name, id):
     # self.name= name
      self.id= id

    def displaypersonal(self):
      print("Name : ", self.name, ", ID: ", self.id)
         #  personal1= Personal("Bhanu",1000);
obj1=Personal("Bhanu",1)
obj1.displaypersonal()
