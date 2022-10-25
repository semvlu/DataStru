cntin = 0
cntpre = 0
cntpost = 0

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = int(k)
 
def insert(root, k):
    if root is None:
        return Node(int(k))
    else:
        if root.val == k:
            return root
        elif root.val < k:
            root.right = insert(root.right, int(k))
        else:
            root.left = insert(root.left, int(k))
    return root 
 
def inorder(root, n):
    global cntin
    if root:
        inorder(root.left, n)
        if(cntin < n - 1):
            print(root.val, end=' ')
            cntin += 1
        else:
            print(root.val)
        inorder(root.right, n)

def preorder(root, n):
    global cntpre
    if root:
        if(cntpre < n - 1):
            print(root.val, end = ' ')
            cntpre += 1
        else:
           print(root.val)
        preorder(root.left, n)
        preorder(root.right, n)

def postorder(root, n):
    global cntpost
    if root:
        postorder(root.left, n)
        postorder(root.right, n)
        if(cntpost < n - 1):
            print(root.val, end = ' ')
            cntpost += 1
        else:
            print(root.val)

# main
a = list(map(int, input().split()))

r = Node(a[0])
for i in (a):
    if i != 0:
        r = insert(r, int(i))

inorder(r, len(a))
preorder(r, len(a))
postorder(r, len(a))
