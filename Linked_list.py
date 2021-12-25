class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,data):
        newnode=Node(data)
        # if inital linked list is empty
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        # add to tail a newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
    def show(self):
        current=self.head
        temp=[]
        temp.append(current.data)
        while current!=self.tail:
            current=current.next
            temp.append(current.data)
        print(temp)
    def swap(self,source,dest):
        """
        we swap:
            previous address(source and dest).next in node together
            address(source and dest).next in node together
        """
        if source!=dest:
            slot1=self.head
            pre_slot1=None
            slot2=self.head
            pre_slot2=None
            # scan for slot source and destination
            while slot1.data !=source:
                pre_slot1=slot1
                slot1=slot1.next
            while slot2.data !=dest:
                pre_slot2=slot2
                slot2=slot2.next
            # found two slot
            if slot1 != None and slot2 != None:
                    
                #swap previous Node:
                    # if preslot1 is normal
                if pre_slot1!=None:
                    pre_slot1.next=slot2
                    #if preslot1 is None => Slot1 is head => swap slot 2 to head
                else: self.head=slot2  
                    # if preslot2 is normal
                if pre_slot2!=None:
                    pre_slot2.next=slot1   
                    #if preslot2 is None => Slot2 is head => swap slot 2 to head
                else: self.head=slot1
                # swap 2 node:
                temp=slot1.next
                slot1.next=slot2.next
                slot2.next=temp
        # do nothing if source and destination equal
        else:
            return

newList=LinkedList()

newList.add(2)
newList.add(3)
newList.add(4)
newList.show()
newList.swap(2,3)
newList.show()