class BMW:
    def max_speed(self):        
        print("My name is BMW. My max speed is : 190")
    def mileage(self):
        print("And my mileage is : 200")
class Ferrari:
    def max_speed(self,):
        print("My name is Ferrari. My max speed is : 250")
    def mileage(self,):
        print("And my mileage is : 300")
obj1=BMW()
obj2=Ferrari()        
for car in (obj1,obj2):
    car.max_speed()
    car.mileage()