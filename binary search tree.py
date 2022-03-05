class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


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


    return root


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
insert(Root,73)
insert(Root,21)
insert(Root,20)
insert(Root,34)
insert(Root,60)
insert(Root,97)

inorder(Root)
delete(Root,48)
print('****************************************')
inorder(Root)
