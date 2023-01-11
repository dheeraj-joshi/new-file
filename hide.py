import os
hide_option=input("you want to hide the folder(y/n): ")

if (hide_option is "y"):
    os.system("attrib +h +r +s")
    print("your folder are hidden")
    d=input("are want to see your files again:")
    if d=="y":
        os.system('attrib -h -r -s')
    else:
        print("ok bye. you files are hidden mode")                  

       
