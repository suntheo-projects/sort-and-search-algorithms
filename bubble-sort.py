
dizi = [2,5,7,-2,77,11,63]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array)- i -1):
            if array[j] > array[j +1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


bubblesort(dizi)
print(dizi)