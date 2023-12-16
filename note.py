# import math
#
# def masofa_aylana_boylab(L):
#     radius = L / 2
#     masofa = math.sqrt((L ** 2) / 2)
#     return masofa
#
# # Kvadrat tomon uzunligi
# uzunlik_kvadrat = int(input("Kvadrat tominini kiriting: "))
#
# # Masofani hisoblash
# masofa_result = masofa_aylana_boylab(uzunlik_kvadrat)
#
# # Natijani chiqarish
# print(f"Aylana ichidagi bo'lkaklar to'rtburchakning uch nuqtasidan masofa: {masofa_result}")



# import math
#
# def find_point_on_circle(radius, distance):
#     circumference = 2 * math.pi * radius
#     angle = (distance / circumference) * 2 * math.pi
#     x = radius * math.cos(angle)
#     y = radius * math.sin(angle)
#     return (x, y)
#
# radius = 5
# distance = 10
# point = find_point_on_circle(radius, distance)
# print(f"The point on the circle is: {point}")



class Person:
    def __init__(self, full_name, job, address):
        self.full_name= full_name
        self.job = job
        self.address = address


    def cool(self):
        print(self.full_name, self.job, self.address)


class Teacher(Person):
    def __init__(self, full_name, job, address, age, number):
        super().__init__(full_name, job, address)    #####  polifarmizim deyiladi
        self.age= age
        self.number = number


    def info(self):
        print(f'ism:{self.full_name} kasbi:{self.job} manzil:{self.address} yosh:{self.age} nomer:{self.number}')


ob=Teacher(full_name=input("Ism="), job=input("kasbi="), address=input("manzil="), age=int(input("yosh=")), number=int(input("number=")))
ob.info()
