class Student: 
    def __init__(self, name): 
        self.__name = name 
  
    def displayName(self): 
        print(self.__name) 
  
s1 = Student("Santhosh") 
s1.displayName() 
  
# Raises an error 
print(s1._Student__name) 