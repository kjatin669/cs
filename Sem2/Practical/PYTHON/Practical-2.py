import os
while True:
    print("1)Create Directory\n2)Remove Directory\n3)Rename Directory\n4)Delete Directory\n5)Displat the present working of file Directory\n6)Create a File and store content in it\n7)Open File\n8)Exit")
    if n==1:
        mdir = str(input("Enter the Name of Directory: "))
        os.mkdir(mdir)
    elif n==2:
        rdir = str(input("Enter the Name of Directory to Remove: "))
        os.rmdir(rdir)
    elif n==3:
        redir = str(input("Enter the Previous File Name: "))
        rndir = str(input("Enter the New File Name: "))
    elif n==4:
        remove = str(input("Enter the Filename: "))
        os.remove(remove)
    elif n==5:
        print(os.getcwd())
    elif n==6:
        fname = str(input("Enter the Filename with Extension: "))
        f = open(fname, 'w')
        fwrite = str(input("Enter the Content to Writ into the file: "))
        f.write(fwrite)
        f.close
    elif n==7:
        fname = str(input("Enter the File Name: "))
        f = open(fname, 'r')
        a = f.read()
        print(a)
        f.close()
    else:
        break
