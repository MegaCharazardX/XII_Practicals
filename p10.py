myfile= open("D:\\ India.txt", "x") 
s= myfile.readlines ()
linecount = len(s)
size=0
for i in s:
    a= len(i)
    size+=a
print (" Size of the file is", size)
print (" No. of lines in the file is", linecount)