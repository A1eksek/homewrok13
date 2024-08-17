'''
Первая задача
'''
# class Person():
#     pass
#
# id_1 = Person()
# setattr(id_1, 'name', 'Vasya')
# setattr(id_1, 'name', 'Masha')
# print(id_1.name)
'''
Вторая задача
'''
# class Person():
#     setup = ['set_name', 'set_age', 'set_work', 'set_study']
#
# id_1 = Person()
#
# for i in id_1.setup:
#     setattr(id_1, i, input())
#
# print(id_1.set_name)
# print(id_1.set_age)
# print(id_1.set_work)
# print(id_1.set_study)
'''Третья задача'''
class Person:
    def __init__(self, hobby, speciality, study):
        self.hobby = hobby
        self.speciality = speciality
        self.study = study

id_1 = Person('danse', 'design', 'college')
print(getattr(id_1, 'hobby'))
print(getattr(id_1, 'speciality'))
print(getattr(id_1, 'study'))






