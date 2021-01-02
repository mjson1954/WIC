def preorder_traverse(T): #전위순회
    if T:  #T is not None
        visit(T)  #print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

def inorder_traverse(T): #중위순회
    if T: #T iS not None
        inorder_traverse(T.left)
        visit(T) #print(T.item)
        inorder_traverse(T.right)

def postorder_traverse(T): #후위순회
    if T:  #T is not None
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)  #print(T.item)

        