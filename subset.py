# class subsets:
#     def __init__(self,s) :
#         a = [[]]
#         for element in s:
#             for i in range(len(a)):
#                 a.append(a[i] + [element])
                
#         print(a)
    
# w=subsets([4,5,6])

    





class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)
   

# class new:
#  def __init__(self,a):
#     d=[[]]
#     for i in a:
#         for e in range(len(d)):
#             d.append(d[e]+[i])
#     print(d)
# v=new([1,2,3])  


# class a:
#     def __init__(self,q):
#      d=[[]]
#      for ele in q:
#             for i in range(len(d)):
#                 d.append(d[i]+[ele])
#      print(d)
# b=a([4,7,1])                 



