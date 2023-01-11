# a=[]
# n=int(input("how much no you want to print:"))
# for i in range(n):
#     a.append((input("enter the elements")))   
# print(a)
   
# a=[1,4,32,56,77,7]
# print(a[::-1])


# def show(n):
#     a=[]
#     for i in range(0,n):
#          if i%3==0 and i%5==0:
#             a.append(i)
#     print(a)        
           
    
# show(100)  
# l=["dheeraj","aashish","aman"]
# for i in range(len(l)):
#       print(i,"  ",l[i])


# #write a function take two list and find the same and different elments of list if elment are same than print in differnt list and not same print this list also
def show(lis1,lis2):
   ans1=[]
   ans2=[]
   for x in lis1:
      if x in lis2:
       ans2.append(x)
   print("same",ans2)      
   for g in lis1:
     if g not in lis2:
      ans1.append(g)
   
   print("diff:",ans1)
show([1,2,3,4,4,65,54,76],[1,2,3]) 

   

# def check(list1,list2):
#     same=[]
#     dif=[]
#     for element in list1:
#         if element in list2:
#             if len(same)==0:
#                 same.append(element)
#             else:
#                 for element2 in same:
#                     if element not  in same:
#                         same.append(element)
#         else:
#             dif.append(element)

#     return same,dif

# print(check([12,34,43,43,544,1,2,3,4],[1,2,3]))


