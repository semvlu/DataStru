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
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = ' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end = ' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end = ' ')

# main
a = list(map(int, input().split()))

r = Node(a[0])
for i in (a):
    if i != 0:
        r = insert(r, i)

inorder(r)
print()
preorder(r)
print()
postorder(r)
print()