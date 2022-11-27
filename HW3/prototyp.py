import sys
cntin = 0
"""
lvl-ord 每個顏色排序後 Last 3 nodes -> 外場  else內場
lvl-ord 1st -> 跳球
外場 & 跳球不能是同一人
if 外場 < 3 or 沒有跳球 -> No game
a team must >=4
--------------------------------------
OUT:
Red team: 紅座號 (小至大, 逗點分隔): in-order / sort
outfield: 紅外場座號 (小至大, 逗點分隔)
jump ball: 紅跳球
Black team: 黑座號(小至大, 逗點分隔)
outfield: 黑外場座號(小至大, 逗點分隔)
jump ball: 黑跳球
--------------------------------------
No game



1. root: Black
2. leaves: Black
3. Red has both children in Black
4. simple path from a given node to any of its leaves
   has an equal #Black
"""

# parent & color
class Node(object):
    def __init__(self, val):
        self.val = val
        self.pa = None
        self.left = None
        self.right = None
        self.color = 1


class RBTree(object):
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Inorder
    #def in_order_helper(self, node):
    #    if node != TNULL:
    #        self.in_order_helper(node.left)
    #        sys.stdout.write(node.val + ",")
    #        self.in_order_helper(node.right)
    #def inorder(self):
    #    self.in_order_helper(self.root)



    # Search the tree
    def search_tree_helper(self, node, key):
        if node == TNULL or key == node.val:
            return node

        if key < node.val:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.pa.color == 1:
            if k.pa == k.pa.pa.right:
                u = k.pa.pa.left
                if u.color == 1:
                    u.color = 0
                    k.pa.color = 0
                    k.pa.pa.color = 1
                    k = k.pa.pa
                else:
                    if k == k.pa.left:
                        k = k.pa
                        self.right_rotate(k)
                    k.pa.color = 0
                    k.pa.pa.color = 1
                    self.left_rotate(k.pa.pa)
            else:
                u = k.pa.pa.right

                if u.color == 1:
                    u.color = 0
                    k.pa.color = 0
                    k.pa.pa.color = 1
                    k = k.pa.pa
                else:
                    if k == k.pa.right:
                        k = k.pa
                        self.left_rotate(k)
                    k.pa.color = 0
                    k.pa.pa.color = 1
                    self.right_rotate(k.pa.pa)
            if k == self.root:
                break
        self.root.color = 0

    def insert(self, key):
        node = Node(key)
        node.pa = None
        node.val = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.pa = y
        if y == None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.pa == None:
            node.color = 0
            return

        if node.pa.pa == None:
            return

        self.fix_insert(node)


    # Print
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "R" if node.color == 1 else "B"
            print(str(node.val) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)
    def print_tree(self):
        self.__print_helper(self.root, "", True)


    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.pa
        while y != self.TNULL and x == y.right:
            x = y
            y = y.pa
        return y

    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.pa
        while y != self.TNULL and x == y.left:
            x = y
            y = y.pa

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.pa = x

        y.pa = x.pa
        if x.pa == None:
            self.root = y
        elif x == x.pa.left:
            x.pa.left = y
        else:
            x.pa.right = y
        y.left = x
        x.pa = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.pa = x

        y.pa = x.pa
        if x.pa == None:
            self.root = y
        elif x == x.pa.right:
            x.pa.right = y
        else:
            x.pa.left = y
        y.right = x
        x.pa = y



    def get_root(self):
        return self.root



def inorder(root, n):
    global cntin
    if root:
        inorder(root.left,n)
        if(cntin < n - 1):
            print(root.k, end=' ')
            cntin += 1
        else:
            print(root.k)
        inorder(root.right,n)


if __name__ == "__main__":
    a = list(map(int, input().split()))

    r = RBTree()
    for i in (a):
        if i != 0:
            r.insert(int(i))

    r.print_tree()