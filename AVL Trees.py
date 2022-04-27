class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def inorder(root):
    if(root):
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


def insert(root,value):
    if root is None:
        return Node(value)

    else:
        if value<=root.value:
            root.left = insert(root.left,value)

        elif value>root.value:
            root.right = insert(root.right,value)

    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    balance = getBalance(root)

    if balance>1 and value< root.left.value:
        return rightRotate(root)

    if balance <-1 and value> root.right.value:
        return leftRotate(root)

    if balance >1 and value > root.left.value:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and value < root.right.value:
         root.right = rightRotate(root.right)
         return leftRotate(root)


    return root

def leftRotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(getHeight(z.left),getHeight(z.right))

    y.height = 1 + max(getHeight(y.left),getHeight(y.right))

    return y

def rightRotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(getHeight(z.left),getHeight(z.right))

    y.height = 1 + max(getHeight(y.left),getHeight(y.right))

    return y

def getHeight(root):
    if not root:
        return 0

    return root.height

def getBalance(root):
    if not root:
        return 0

    return getHeight(root.left)-getHeight(root.right)

    


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left

    return current

def delete(root,value):
    if root is None:
        return root

    if value<root.value:
        root.left = delete(root.left,value)

    elif value>root.value:
        root.right = delete(root.right,value)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return root

        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = delete(root.right,temp.value)

    return root
        


Root = Node(48)
Root = insert(Root,21)
Root = insert(Root,20)
Root = insert(Root,34)
Root = insert(Root,40)
Root = insert(Root,73)
inorder(Root)

