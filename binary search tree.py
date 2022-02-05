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


Root = Node(48)
insert(Root,73)
insert(Root,21)
insert(Root,20)
insert(Root,34)
insert(Root,60)
insert(Root,97)

postorder(Root)
