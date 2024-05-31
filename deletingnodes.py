class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next = head 
    return temp
 
 
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
    temp = Node(ele)
    index = 0 
    currentNode = head 
 
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
 
 
 
def deleteTailNode(head):
    if head == None or head.next == None:
        return None
 
    previous = None 
    currentNode = head 
 
    while currentNode.next != None:
        previous = currentNode 
        currentNode = currentNode.next 
 
    previous.next = None
    return head
 
def deleteHeadNode(head):
    if head == None:
        return head 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
 
 
 
 
 
 
 
def deleteNodeAtSpecificPosition(head, position):
    index = 0 
    currentNode = head 
    while index != position - 1:
        index += 1 
        currentNode = currentNode.next 
 
    # currentNode will point to immediate previous node of position 
    nodeToBeDeleted = currentNode.next
    nextNode = nodeToBeDeleted.next 
 
    nodeToBeDeleted.next = None 
    currentNode.next = None 
    currentNode.next = nextNode
 
    return head
 
 
 
 
 
 
 
 
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
 
#head =insertAtSpecificPosition(head, 3, 101)
head = deleteNodeAtSpecificPosition(head, 4)
printLinkedList(head)