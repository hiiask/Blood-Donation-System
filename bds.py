print("For admin enter 1 and user enter 0")
a=int(input("Give input  "))
if (a==0):
    print("If you want to register enter 2 otherwise enter any other number.")
    y=int(input())
    if (y==2):
        x=str(input("Enter your Name to register in our system and please write \\n on end to change the line.   "))
        f=open("bds.txt", "a")
        f.write(x)
        f.close()
        print("Congratulations you have been registered with our system.\n")
    else:
        pass
    z=int(input("Press 3 if you want to know about blood donation camps otherwise ignore this message.   "))
    if (z==3):
        naam=str(input("Enter Hospital name.   "))
        f=open("bdc.txt","r")
        out=[i for i in f if naam in i]
        print(str(out))

if (a==1):
    print("If you want to see and read all the data press 4 or if you want to add something in file press 5.")
    ra=int(input())
    if(ra==4):
        q=open("bds.txt", "r")
        print(q.read())
    if(ra==5):
        print("if you want to replace a string enter 6 or if you want to add a new string enter 7 or if you want to add any information about blood donation camp enter 8.")
        replace=int(input())
        if (replace==6):
            d=str(input("Enter the string which you want to replace.  "))
            e=str(input("Enter the new string which is placed in place on older one.  "))
            fin = open("bds.txt", "rt")
            data = fin.read()
            data = data.replace(d,e)
            fin.close()
            fin = open("bds.txt", "wt")
            fin.write(data)
            fin.close()
            print("Modified text file is.\n")
            print("                          ")
            k=open("bds.txt", "r")
            print(k.read())
        if(replace==7):
            text_file = open("bds.txt", "a")
            z=str(input("Enter the string which you want to add in text file, in the given format    'Name of DonarTabTabTabTabBlood GroupTabTabTabTabHospital in which donatedTabTabTabTabAddress of donarTabTabEmail id of donar'  "))
            m=text_file.write("\n"+z)
            text_file.close()
            print("Modified text file is.\n")
            print("                          ")
            k=open("bds.txt", "r")
            print(k.read())
        if(replace==8):
            text_file = open("bdc.txt", "a")
            q=str(input("Enter the string which you want to add in text file,, in the given format    'Hospital in which camp heldTabTabTabTabTabDate and TimeTabTabTabEmail id of hospital'  "))
            w=text_file.write("\n"+q)
            text_file.close()
            print("Modified text file is.\n")
            print("                          ")
            e=open("bdc.txt", "r")
            print(e.read())
