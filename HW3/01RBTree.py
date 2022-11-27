Rteam = []
Ro = []
Bteam = []
Bo = []
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current

            # 2a: node w/ 2 red children
            if parent.left.red == True and parent.right.red == True:
                parent.red = True
                parent.left.red = False
                parent.right.red = False

            # 2b: 2 cons red nodes
            if parent.red == True:
                if parent.parent.red == True:
                    if parent == parent.parent.left: # xL
                        if parent.parent == parent.parent.parent.left: # LL
                            self.Lrotate(parent)
                            self.Lrotate(parent)
                        elif parent.parent == parent.parent.parent.right: # RL
                            self.Rrotate(parent)
                            self.Lrotate(parent)
                    elif parent == parent.parent.right: # xR
                        if parent.parent == parent.parent.parent.left: # LR
                            self.Lrotate(parent)
                            self.Rrotate(parent)
                        elif parent.parent == parent.parent.parent.right: # RR
                            self.Rrotate(parent)
                            self.Rrotate(parent)


            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return


        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.Rrotate(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.Lrotate(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.Lrotate(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.Rrotate(new_node.parent.parent)
        self.root.red = False

    # L rotate
    def Lrotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # R rotate
    def Rrotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)


def lvlord(root):
    h = height(root)
    
    for i in range(1, h+1):
        curlvl(root, i)

# Print the node at curlvl
def curlvl(root, level):
    global Rteam
    if root is None or root.val == 0:
        return
    if level == 1:
        if root.red == False:
            Rteam.append(root.val)
        else:
            Bteam.append(root.val)
        #print(root.val, end=" ")
    elif level > 1:
        curlvl(root.left, level-1)
        curlvl(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
 
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# main
t = RBTree()
a = list(map(int, input().split()))

for i in (a):
    if i != 0:
        t.insert(int(i))


lvlord(t.root)

if (len(Rteam) < 4) or (len(Bteam) < 4):
    print("No game")

else:
# Red Team
    Rj = Rteam[0]
    for i in range(len(Rteam) - 1, len(Rteam) - 4, -1):
        Ro.append(Rteam[i])
    Ro.sort()

    Rteam.sort()
    print("Red team:", end=' ')
    for i in range(len(Rteam)):
        if i < (len(Rteam) - 1):
            print(Rteam[i], end=',')
        else:
            print(Rteam[i])

    # Red outfield

    print("outfield:", end=' ')
    for i in range(len(Ro)):
        if i < (len(Ro) - 1):
            print(Ro[i], end=',')
        else:
            print(Ro[i])

    # Red jump
    print("jump ball:", Rj)


    # Black Team
    Bj = Bteam[0]
    for i in range(len(Bteam) - 1, len(Bteam) - 4, -1):
        Bo.append(Bteam[i])
    Bo.sort()

    Bteam.sort()
    print("Black team:", end=' ')
    for i in range(len(Bteam)):
        if i < (len(Bteam) - 1):
            print(Bteam[i], end=',')
        else:
            print(Bteam[i])

    # Black outfield
    print("outfield:", end=' ')
    for i in range(len(Bo)):
        if i < (len(Bo) - 1):
            print(Bo[i], end=',')
        else:
            print(Bo[i])

    # Black jump
    print("jump ball:", Bj)