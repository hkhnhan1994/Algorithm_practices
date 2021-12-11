"""
    Order number by ascending and descending
    Using Recursion
"""

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_children(self,data):
        if self.data==data:
            # data avalid cant do duplicate
            return
        else:
            if self.data > data:
                # add data in lelf side
                if self.left:
                    #if left avalid branch, let's add more add_children
                    self.left.add_children(data)
                else:
                    #if left avalid branch, let's add node into left branch
                    self.left=BinaryTreeNode(data)
            else: 
                if self.right:
                    #if right avalid branch, let's add more add_children
                    self.right.add_children(data)
                else:
                    #if right avalid branch, let's add node into right branch
                    self.right=BinaryTreeNode(data)
    #order by asc BinaryTreeNode using Recursion
    def in_order_traveller(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traveller()
        elements.append(self.data)

        if self.right:
             elements+=self.right.in_order_traveller()
        return elements
    def search(self,data):
        if data== self.data:
            return True
        if data<self.data:
            #search on left side
            if self.left:
                self.left.search(data)
            else:
                return False
        if data>self.data:
             #search on right side
            if self.right:
                self.right.search(data)
            else:
                return False
def build_tree(elements):
    root=BinaryTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_children(elements[i])
    return root

if __name__ == "__main__":

    elements=[9,3,2,8,10,15,0,5,4,1,6,11,13,16,12,7]
    new_tree=build_tree(elements)
    # sort elements by ascending order
    asc_elements=(new_tree.in_order_traveller())
    print(asc_elements)
    #sort elements by descending order
    desc_elements=[]
    for ele in range(0,len(asc_elements)):
        desc_elements.append(asc_elements[len(asc_elements)-ele-1])
    print(desc_elements)