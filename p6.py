import csv
prodata= [["PID", "PNAME", "COST", "QUANTITY"], 
        ["P", "BRUSH", 50, 200],
        [ "P" "TOOTHPASTE", 120, 150],
        ["P" "SOAP", 40,300], 
        ["P", "SHEETS", 100, 500],
        [ "P", "PEN", 10, 250]]
23
def write ():
    a= open("PRODUCT. csv", "w", newline="") 
    c= csv.writer (a)
    c. writerows (prodata)
def read ():
    a= open("PRODUCT⋅ CSV", "y") 
    c= csv.reader (a) 
    for i in c: 
        print (i)
write() 
read ()