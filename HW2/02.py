import sys
cnt = 0
rot = list()
class TreeNode(object):
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    
    def insert(self, root, k):
        global cnt, rot
        if not root:
            return TreeNode(k)
        elif k < root.k:
            root.left = self.insert(root.left, k)
        else:
            root.right = self.insert(root.right, k)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))


        blnc = self.getBalance(root)
        if blnc > 1: # Lx
            cnt += 1
            if k < root.left.k: # LL
                rot.append("LL")
                return self.rightRotate(root)
                
                
            else: # LR
                rot.append("LR")
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
                

        if blnc < -1: # Rx
            cnt += 1
            if k > root.right.k: # RR
                rot.append("RR")
                return self.leftRotate(root)
                

            else: # RL
                rot.append("RL")
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
                

        return root

    def delete(self, root, k):
        global cnt, rot
        if not root:
            return root
        elif k < root.k:
            root.left = self.delete(root.left, k)
        elif k > root.k:
            root.right = self.delete(root.right, k)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.k = temp.k
            root.right = self.delete(root.right, temp.k)
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        blnc = self.getBalance(root)
# R0: LL, RR
# R1: LL, RL
#R-1: RR, LR
        if blnc > 1: # Lx
            cnt += 1
            if self.getBalance(root.left) > 0: # LL (R1)
                rot.append("R1")
                return self.rightRotate(root)

            elif self.getBalance(root.left) == 0: # LL (R0)
                rot.append("R0")
                return self.rightRotate(root)

            else: # LR (R-1)
                rot.append("R-1")
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if blnc < -1: # Rx
            cnt += 1
            if self.getBalance(root.right) < 0: # RR (R-1)
                rot.append("R-1")
                return self.leftRotate(root)

            elif self.getBalance(root.right) == 0: # RR
                rot.append("R0")
                return self.leftRotate(root)

            else: # RL
                rot.append("R1")
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.k, end = ' ')
            self.inorder(root.right)


# main
t = AVLTree()
root = None 

# inital input

instr = input()
ar = []
for i in instr.split(","):
    try:
        ar.append(int(i))
    except ValueError:
        pass

for i in ar:
    root = t.insert(root, i)

# commands begin from ln 2
while True:
    line = input()

    if line:
        num = []
        for i in line.split():
            try:
                num.append(int(i))
            except ValueError:
                pass

        if line[0] == 'I':
            t.insert(root, num[0])
        elif line[0] == 'D':
            t.delete(root, num[0])

    else:
        break


t.inorder(root)
print()
print(cnt)
for i in range(0,len(rot)):
    if(i != len(rot) - 1):
        print(rot[i], end=',')
    else:
        print(rot[i])