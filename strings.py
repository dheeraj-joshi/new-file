x="ab+bc+db"
c=list(x)
q=c[1]
w=c[0]
r=c[2]
t=c[4]
y=c[3]
u=c[5]
i=c[7]
o=c[6]
p=(q+w+r+t+y+u+i+o)
print(p)
print(type(p))

a="Dheeraj\n"
p=a*4

print(p)

a=int(input("enter the number: "))


a=int(input("enter the numbers: "))
f=str(a)
print(f)
print(type(f))


z=input("Enter your string: ")
if "a" in z:
    print("a:",z.count("a"))        
if "e" in z:
    print("e:",z.count("e")) 
if "i" in z:
    print("i:",z.count("i"))   
if "o" in z:
    print("o:",z.count("o")) 
if "u" in z:
    print("u:",z.count("u")) 
else:
    print("consonant",z) 


count_vowel=""
count_consonant=""
a=input("enter the string")
vowels="aeiou"
for i in a:
    if i in vowels:
        count_vowel+=i
    else:
        count_consonant+=i 
print('count vowels:',count_vowel) 
print('count cosonants:',count_consonant)           











     
        
        
        













