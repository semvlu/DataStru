class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = k
 
def insert(root, k):
    if root is None:
        return Node(k)
    else:
        if root.val == k:
            return root
        elif root.val < k:
            root.right = insert(root.right, k)
        else:
            root.left = insert(root.left, k)
    return root 
 
def inorder(root, n):
    cnt = 0
    if root:
        inorder(root.left, n)
        if(cnt < n - 1):
            print(root.val, end = ' ')
            cnt += 1
        else:
            print(root.val)
        inorder(root.right, n)

def preorder(root, n):
    cnt = 0
    if root:
        if(cnt < n - 1):
            print(root.val, end = ' ')
            cnt += 1
        else:
           print(root.val)
        preorder(root.left, n)
        preorder(root.right, n)

def postorder(root, n):
    cnt = 0
    if root:
        postorder(root.left, n)
        postorder(root.right, n)
        if(cnt < n - 1):
            print(root.val, end = ' ')
            cnt += 1
        else:
            print(root.val)

# main
a = list(map(int, input().split()))

r = Node(a[0])
for i in (a):
    if i != 0:
        r = insert(r, i)

inorder(r, len(a))
print()
preorder(r, len(a))
print()
postorder(r, len(a))
print()