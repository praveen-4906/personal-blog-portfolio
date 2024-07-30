array = []

def found(searchelement,index) :
    print("The search element ",searchelement," found at index : ",index)

def search(array,n) :
    isfound = False
    searchelement = int(input("Enter the search element : "))
    for j in range (0,n) :
        if searchelement == array[j] :
            found(searchelement, j)
            isfound = True
    else :
        if isfound == False :
            print("Element not found")

n = int(input("Enter the number of array elements : "))

for i in range (0,n) :
    print("Enter the element ",i+1,end=' : ')
    num = int(input())
    array.append(num)

print("The array you entered is ",array)

choice = input("Do you want to search an element (y/n) : ")
if choice == 'y' :
    search(array,n)