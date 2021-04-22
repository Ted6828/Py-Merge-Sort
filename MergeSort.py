MergeSort = []

def Merge(Array):
    length = len(Array)
    if length >1:
        HalfLength = int(length/2)
        Array1 = list.copy(Array)
        Array2 = list.copy(Array)
        for i in range (HalfLength):
             Array1.pop(len(Array1)-1)
             Array2.pop(0)
        Array1 = Merge(Array1)
        Array2 = Merge(Array2)
        return Merge2(Array1, Array2)
    else:
        return Array 

def Merge2(Array1, Array2):
    Array3 = []
    Var1 = 0
    Var2 = 0
    while Var1 < len(Array1) and Var2 < len(Array2):
        if Array1[Var1] < Array2[Var2]:
            Array3.append(Array1[Var1])
            Var1 = Var1 + 1
        else:
            Array3.append(Array2[Var2])
            Var2 = Var2 + 1
    while len(Array3) != len(Array1) + len(Array2):
        if Var1 >= len(Array1):
            Array3.append(Array2[Var2])
            Var2 = Var2 + 1
        elif Var2 >= len(Array2):
            Array3.append(Array1[Var1])
            Var1 = Var1 + 1
    return Array3

Values = int(input("Enter the number of values (Has to be even!) ... : "))
for i in range(0, Values):
    pog = int(input())
    MergeSort.append(pog)
print(*Merge(MergeSort),end=" ...Is the sorted list!")
