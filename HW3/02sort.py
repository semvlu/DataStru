"""

Bubble: 2 elem in the 5th swap ; seq after swap

Insertion: seq after the 5th insertion

Selection: minimum in the 5th selection; seq after swap

sorted seq


Bubble: 28, 41; 21 24 15 20 19 28 30 20 28 41 13 12 33 25 7
Insertion: 15 20 21 24 28 19 30 41 20 28 13 12 33 25 7
Selection: 19; 7 12 13 15 19 20 30 41 20 28 28 24 33 25 21
7 12 13 15 19 20 20 21 24 25 28 28 30 33 41
"""

# bubble
def bubble(a, n):
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def bubbleAlt(a, n):
    bub = 0
    _5th = []
    for i in range(n):
        for j in range(n - i - 1):

            if a[j] > a[j+1]:
                if bub == 4:
                    a[j], a[j+1] = a[j+1], a[j]
                    _5th.append(a[j])
                    _5th.append(a[j+1])
                    return _5th
                a[j], a[j+1] = a[j+1], a[j]
                bub += 1

            if bub == 5:
                break



# insertion
def insertion(a, n):
    for i in range(1, n):
        tmp = a[i]
        j = i - 1

        while(j >= 0 and tmp < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp

def insertionAlt(a, n):
    for i in range(1, 5):
        tmp = a[i]
        j = i - 1

        while( j >= 0 and tmp <= a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp


# selection
def selection(a, n):
    for i in range(n):
        pos = i
        for j in range(i + 1, n): 
            if a[j] < a[pos]:
                pos = j

        a[i], a[pos] = a[pos], a[i]


def selectionAlt(a, n):
    sel = 0
    for i in range(n):
        pos = i
        for j in range(i + 1, n): 
            if a[j] < a[pos]:
                pos = j

        sel += 1
        if sel == 5:
            s = a[pos]
            a[i], a[pos] = a[pos], a[i]
            break
        a[i], a[pos] = a[pos], a[i]
    
    return s


arr = list(map(int, input().split()))

#arr = [21, 24, 28, 15, 20, 19, 30, 41, 20, 28, 13, 12, 33, 25, 7]

# implement bubble alt
arr4bub = arr.copy()
bubtmp = bubbleAlt(arr4bub, len(arr4bub))

print("Bubble:", end=' ')
for i in range(2):
    if i == 0:
        print(bubtmp[i], end=', ')
    elif i == 1:
        print(bubtmp[i], end='; ')

for i in range(len(arr4bub)):
    if i < (len(arr4bub)-1):
        print(arr4bub[i], end=' ')
    else:
        print(arr4bub[i])

# implement insertion alt
arr4ins = arr.copy()
insertionAlt(arr4ins, len(arr4ins))

print("Insertion:", end=' ')
for i in range(len(arr4ins)):
    if i < (len(arr4ins)-1):
        print(arr4ins[i], end=' ')
    else:
        print(arr4ins[i])

# implement selection alt
arr4sel = arr.copy()
mini_5 = selectionAlt(arr4sel, len(arr4sel))

print("Selection:", end=' ')
print(mini_5, end='; ')
for i in range(len(arr4sel)):
    if i < (len(arr4sel)-1):
        print(arr4sel[i], end=' ')
    else:
        print(arr4sel[i])

# final sorted
bubble(arr, len(arr))
for i in range(len(arr)):
    if i < (len(arr)-1):
        print(arr[i], end=' ')
    else:
        print(arr[i])
