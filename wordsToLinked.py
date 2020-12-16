class Node: 
  
    def __init__(self, data): 
        self.data = data   
        self.next = None   
  
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  

def wordsToLinked(n): 
    llist = LinkedList() 
  
    llist.head = Node(1)
    for i in range(2,n+1):
        newNode = Node(i)
        newNode.data = i
        llist.head.next = newNode
        nextNode = Node(i+1)
        newNode.next = nextNode
        nextNode = newNode
    nextNode.next = None
  
