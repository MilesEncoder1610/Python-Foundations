n=int(input("Enter The Total Number Of Elements:"))
mylist=[int(input("Enter The Number:")) for i in range(n)]
ch=input("Enter Yes/No to start Execution:")
while(ch=="Yes"):
    print("The list is:",mylist)
    print("Following are The List Of Operations That can be performed by the Program:")
    print("1)Appending Element/List:")
    print("2)Insert Element:")
    print("3)Modifying an Element:")
    print("4)Deleting Element with Value/Index:")
    print("5)Sort in ascending/descending order:")
    print("6)Display The list:")
    print("7)Exit The Loop:")
    choice=int(input("Enter The Number for operation:"))
    if(choice==1):
        a=input("List/Element?:")
        if(a=="Element"):
            ele=int(input("Enter Element To Join:"))
            mylist.append(ele)
        else:
            k=int(input("Enter The Count Of Numbers To Be Added:"))
            list1=[int(input("Enter The Number:")) for i in range(k)]
            mylist.append(list1)
    elif(choice==2):
        k=int(input("Enter The Position for Item Insertion:"))
        a=input("List/Element?:")
        if(a=="Element"):
            ele=int(input("Enter Element To Insert:"))
            mylist.insert(k-1,ele)
        else:
            k1=int(input("Enter The Count Of Numbers to be added:"))
            list1=[int(input("Enter The Number:")) for i in range(k1)]
            mylist.insert(k-1,list1)
    elif(choice==3):
        k=int(input("Enter The Position for Item Modification:"))
        a=input("List/Element?:")
        if(a=="Element"):
            ele=int(input("Enter Element To Modify:"))
            mylist[k-1]=ele
        else:
            k1=int(input("Enter The Count Of Numbers to be added:"))
            list1=[int(input("Enter The Number:")) for i in range(k1)]
            mylist[k-1]=list1
    elif(choice==4):
        a=input("Element/Position?:")
        if(a=="Element"):
            ele=int(input("Enter Element To Delete:"))
            mylist.remove(ele)
        else:
            k=int(input("Enter The Position for Item Deletion:"))
            mylist.pop(k-1)
    elif(choice==5):
        a=input("Ascending/Descending?:")
        if(a=="Ascending"):
            mylist.sort()
        else:
            mylist.sort(reverse=True)
    elif(choice==6):
        print("The List Is:",mylist)
    elif(choice==7):
        print("Exiting From Loop; No more Operations.")
        print("Are you sure?")
        ch=input("Yes/No:")
        if(ch=="Yes"):
            break
        else:
            ch="Yes"
            continue
    else:
        print("Please Enter A Valid Number(1-7)!")
        print("Do you wish to continue?")
        ch=input("Yes/No:")
        continue
    print("Operation Has Been Completed Successfully:")
    print("Do you wish to Repeat?")
    ch=input("Yes/No:")
    continue
