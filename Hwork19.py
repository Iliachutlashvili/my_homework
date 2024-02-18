class ListNode:
    def __init__(self, value):
        self.value = value   # იქმნება ნოუდი მიღებული ველიუთი
        self.next = None  # შემდეგი ნოუდი თავიდან არაფერი არ არის ანუ 'None'


class LinkedList:
    def __init__(self, value):
        self.head = ListNode(value)  # იქმნება საწყისი ნოუდი რომელიც გადაეცემა ზედა ლისტნოუდის ველიუს.
        self.length = 1   # საწყისი ნოუდი = 1. 

    def append(self, value):
        current_node = self.head   # 

        while current_node.next is not None:  # მიდის ციკლის მარჯვენა მხარეს სადამ ბოლოში არ გავა.
            current_node = current_node.next

        new_node = ListNode(value) # ქმნის ახალ ნოუდს და სვავს სიის ბოლოში.
        current_node.next = new_node
        self.length += 1      

    def insert(self, value, index):  # აქ ცოტა დავიბენი და ვერ მივხვდი ... 
        last_index = self.length - 1 
        i = 0

        if index == 0:  
            old_head = self.head
            self.head = ListNode(value)
            self.head.next = old_head
            self.length += 1

        elif index == last_index+1:   
            self.append(value)

        elif 0 < index < last_index + 1: 
            current_node = self.head

            while i != index-1: # სადამ საჭირო ინდექსამდე არ მიდის აგრძელებს მოძრაობას მარჯვნივ.
                current_node = current_node.next
                i += 1
                
            new_node = ListNode(value)  # როდესაც საჭირო ინდექს მივადგებით ამ დროს ხდება ჩანაცვლება ახალი ნოუდით.
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

        elif index > last_index + 1 or index < 0:  # როდესაც არასწორი ინდექსი შეგვყავს და ვცდებით ინდექსების რეინჯს გამოდის ერორი.
            print("Index Is Out Of Range")


    def printList(self):
        current_node = self.head
        print(f"{current_node.value} ->", end="")  # პრინტავს ჰედ ნოუდს

        while current_node.next is not None:  # მიყვება ნოუდებს და პრინტავს სათითაოდ ყველას ველიუს
            current_node = current_node.next
            print(f" {current_node.value} ->", end="") # ამჟამინდელ ანუ Current ნოუდს პრინტავს. 



linked_list = LinkedList(0)


linked_list.append(1)
linked_list.append(5)
linked_list.insert(2, 2)
linked_list.insert(3, 3)
linked_list.insert(4, 4)
linked_list.insert(7, 0)
linked_list.insert(10, 7)
linked_list.printList()
print(linked_list.length)