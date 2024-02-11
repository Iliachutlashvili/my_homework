class Node:
    def __init__(self, key):
        self.left = None    # მარცხენა ჩაილდი არის - ნანი (არაფერი)
        self.right = None   # მარჯვენა ჩაილდი არის - ნანი (არაფერი)
        self.val = key      # ქი აძლევს ველიუს ჩვენს ნოუდებს 

def insert(root, key):
    if root is None:        # თუ რუთი არის ცარიელი,ვანიჭებთ ზევით შექმნილ ქის და ვაბრუნებთ
        return Node(key)
    else:
        if root.val < key:   #  თუ ქი იქნება რუთზე მეტი ველიუთი, ვსვავთ მარჯვნივ 
            root.right = insert(root.right, key)
        else:                #  სხვა დანარჩენ შემთხვევაში ვსვავთ მარცხნივ
            root.left = insert(root.left, key)
    return root             # ვაბრუნებთ რუთს რო იმუშაოს კოდმა.

def inorder_traversal(root): 
    if root:
        inorder_traversal(root.left)    # მარცხნივ ჩასასმელი რუთი
        print(root.val)                 
        inorder_traversal(root.right)   # მარჯვნივ ჩასასმელი რუთი.

# რუთი თავიდან არის არაფერი შემდეგ ვაინსერტებთ რენდომად ციფრებს და ზევით დაწერილი insert მეთოდით იგებს თუ საიდ ჩასვას მომდევნო ციფრი
if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print("Inorder traversal of the tree:")
    inorder_traversal(root)

    # იმედია სწორად გავიგე დავალება და სწორად მოვძებნე :D 