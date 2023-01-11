# class subsets:
#  s=[4, 5, 6]
#  a = [[]]
#  for element in s:
#         for i in range(len(a)):
#             current_subset = a[i]
#             a.append(current_subset + [element])
    
# w=subsets()
# print(w.a)

# # class subsets:
# s=[4, 5, 6]
# subset = [[]]
# for element in s:
#          for i in range(len(subset)):
#               current_subset=subset[i]
#               subset.append(current_subset+[element])
# print(subset)     
    

# # c=subsets()
# # # print(c.subset)
# a=(4,5,60)
# list1=[]
# for i in range(len(a)):
#    for j in range(i+1,len(a)+1):
#     list1.append(a[i:j])
# print(list1)    



class Student:
    def show(self,name,roll):
        self.name=name
        self.roll=roll
s=Student()
s.show("dheeraj",23)

print(s.__dict__)



# class Student: 
#     def __init__(self, student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name 
# student = Student('V12', 'Frank Gibson', 'V')
# print(student.__dict__)




