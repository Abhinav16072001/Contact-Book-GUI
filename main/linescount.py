fh=open("hello.py")
c=0
for i in fh:
    if i=="\n":continue
    else:
        c=c+1

print("Total Lines :",c)
