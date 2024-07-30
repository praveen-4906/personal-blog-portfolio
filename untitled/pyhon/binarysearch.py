#searching

array = []

def result (found,element) :
    if found == True :
        print("The element ",element," found in the array")
    else :
        print("The element ",element," not found in the array")


def search (array,num) :
    element = int(input("Enter the element to be searched : "))
    j = 0
    found = False
    while found == False and j < num :
        if array[j] == element :
            found = True
        else :
            found = False
        j += 1
    result(found,element)



num = int(input("Enter the number of array elements : "))
i = 0
while i < num :
    print("Enter the element ",i,end = ' : ')
    n = int(input())
    array.append(n)
    i = i+1

print("The array you entered is : ",array)
choice = input("Do you want to search an element : ")
search(array,num) if choice == 'y' else exit()