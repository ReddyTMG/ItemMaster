#nested loop
#for-while-for    for-for

def P6Q2():
    #2 dimensional
    for y in range(4):       #-> range(start, end-1, inc)  y-> 0, 1, 2, 3, 4
                             #-> row, y-axis (outer loop)
        for x in range(5):   #-> col, x-axis (inner loop)
            print("(%d,%d)"%(y,x),end="   ")  #print it horizontally
        print()
    
    
def readFile():
    fileobj=open("itmLST.txt", "r")
    lines=fileobj.readlines()  #convert to a list (each line= 1 element)
    itmLst=[]
    for line in lines:
        tLst=line.strip("\n").split("|")
        #strip -> strip "\n" at end of the line
        #split -> convert the string to a list, based on "|"
        itmLst.append(tLst)
    fileobj.close()
    return itmLst

def displayRecOld():
    for y in range(len(itmLst)):
        for x in range(len(itmLst[y])):
            print("%s"%itmLst[y][x],end="   ")
        print()

def displayRec(itmLst):
    print("ItemCode   ItemDesc                UOM     WTPrice    Price   ")
    print("-"*60)
    for i in range(len(itmLst)): #using reference
        #print(itmLst[idx])
        print("%8s   %-20.20s    %-4.4s   %4d       %6.2f"%(itmLst[i][0],
                itmLst[i][1],itmLst[i][2],int(itmLst[i][3]),float(itmLst[i][4])))
    print("-"*60)

def removalByItem():
    lst2=[5,0,1,23,5,0,23]
    for x in lst2:
    if x==5:
        lst2.pop(lst2.index(x))
        
itmMLst=readFile()
display(itmMLst)
