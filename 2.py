class cat:
     def __init__(self,name,age):
          self.name = name
          self.age = age
     def info(self):
       print(f"i am a cat my name is {self.name} i am {self.age} years old")

     def make_sound(self):
         print("meaow")


class dog:
    def __init__(self,name,age):
          self.name = name
          self.age = age
    def info(self):
       print(f"i am a dog my name is {self.name} i am {self.age} years old")

    def make_sound(self):
         print("bark")

cat1 = cat("tom",3)
cat2 = cat("happy",2)
dog1 = dog("jolly",3)
dog2 = dog("pablo",2)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()

for animal in (cat2,dog2):
    animal.make_sound()
    animal.info()
    

