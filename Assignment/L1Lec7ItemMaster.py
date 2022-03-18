
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
    
    
#CRUD maintenance of item Master
def displayRec(itmLst):
    print("ItemCode   ItemDesc                UOM     WTPrice    Price   ")
    print("-"*60)
    for i in range(len(itmLst)): #using reference
        #print(itmLst[idx])
        print("%8s   %-20.20s    %-4.4s   %4d       %6.2f"%(itmLst[i][0],
                itmLst[i][1],itmLst[i][2],int(itmLst[i][3]),float(itmLst[i][4])))
    print("-"*60)

def addNewitem(itmLst):   #mainItem(itmLst, opt):
    loop=True
    step=1
    while loop:
        if step==1:
            itm=    input("Enter item              <Q>uit >>")
            if itm=="Q":
                step=99
            elif len(itm) !=8:
                print("Invalid item code added")
            elif itm in [x[0] for x in itmLst]:  #else:
                print("Item code already exist")
            else:  #need to check if item exists
                step=step+1
        if step==2:
            itmDesc=input("Enter item Description  <Q>uit >>")
            if itmDesc=="Q":
                step=99
            else:
                step+=1
        if step==3:
            UOM=    input("Enter item UOM          <Q>uit >>")
            if UOM=="Q":
                step=99
            else:
                step +=1
        if step==4:
            wtPr=   input("Enter item weight price <Q>uit >>")
            if wtPr=="Q":
                step=99
            elif not wtPr.isdigit():
                print("Invalid weight price entered")
            else:
                step=step+1
        if step==5:
            itmPr=   input("Enter item price        <Q>uit >>")
            if itmPr=="Q":
                step=99
            else:  #need to check for floating point number
                step +=1

        if step==6:  #complete input
            tLst=[itm, itmDesc, UOM, wtPr, itmPr]
            itmLst.append(tLst)
            loop=False
        if step==99:
            loop=False
    return itmLst  

def delItem(itmLst):
    loop=True
    step=1
    while loop:
        if step==1:
            itm=    input("Enter item              <Q>uit >>")
            if itm=="Q":
                step=99
            elif itm not in [x[0] for x in itmLst]:
                print("Item code Found")
            else:  #need to check if item exists
                step=step+1
        if step==2:
            idx=[x[0] for x in itmLst].index(itm)
            itmLst.pop(idx)
            #need to pop it from itmLst
            #print("Remove successful")
            loop=False

        if step==99:
            loop=False
    return itmLst
    
def updItem(itmLst):
    #print("akan datang")
    loop=True
    step=1
    while loop:
        if step==1:
            itm=    input("Enter item              <Q>uit >>")
            if itm=="Q":
                step=99
            elif itm not in [x[0] for x in itmLst]:
                print("Item code Found")
            else:  #need to check if item exists
                step=step+1
        if step==2:
            itmDesc=input("Enter item Description  <Q>uit >>")
            if itmDesc=="Q":
                step=99
            else:
                step+=1
        if step==3:
            UOM=    input("Enter item UOM          <Q>uit >>")
            if UOM=="Q":
                step=99
            else:
                step +=1
        if step==4:
            wtPr=   input("Enter item weight price <Q>uit >>")
            if wtPr=="Q":
                step=99
            elif not wtPr.isdigit():
                print("Invalid weight price entered")
            else:
                step=step+1
        if step==5:
            itmPr=   input("Enter item price        <Q>uit >>")
            if itmPr=="Q":
                step=99
            else:  #need to check for floating point number
                step +=1

        if step==6:  #complete input for update
            tLst=[itm, itmDesc, UOM, wtPr, itmPr]
            #list comphresion to locate pos/record
            idx=[x[0] for x in itmLst].index(itm)
            itmLst[idx]=tLst
            loop=False
            
        if step==99:
            loop=False
    return itmLst

def saveFile(itmLst):
    wStr=""
    for rec in itmLst:
        wStr += "|".join(rec)+"\n"
    f=open("itmLST.txt", "w")
    f.write(wStr)
    f.close()

itmLst=readFile()
loop=True
while loop:
    displayRec(itmLst)
    print("<A>dd new item  <U>pdate  <D>elete <S>ync File <Q>uit")
    opt=input("Option >> ").upper()
    if opt=="Q":
        loop=False
    elif opt=="A":  #need more validation in addNewitem()
                    #elif opt in ["A","D","U"]:
        itmLst=addNewitem(itmLst)#itmLst=maintItem(itmLst,opt)
    elif opt=="D":
        itmLst=delItem(itmLst)
    elif opt=="U":
        itmLst=updItem(itmLst)
    elif opt=="S":
        saveFile(itmLst)
    else:
        print("Invalid option entered")
        






        
