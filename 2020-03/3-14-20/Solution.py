#main() contains a test case for removeElement()
#This one took a while for me to figure out how to do in O(n) time.
#I ended up traversing the list twice at the same time where the
#second traversal lagged behind the first by k nodes. When the first
#traversal hits the end, I can remove the kth last element with the
#second traversal.


class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

def main():
    node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print("Original Linked List:")
    printLinkedList(node)
    newNode = removeElement(node, 2)
    print("Updated Linked List:")
    printLinkedList(newNode)

#Head is head of a singly linked list, will remove the k-th last element from the list
def removeElement(head, k):
    firstNode = head
    secondNode = head
    lead = 0

    foundEnd = False
    while not foundEnd:
        firstNode = firstNode.link
        if(lead == (k+1)):
            secondNode = secondNode.link
        else:
            lead += 1

        if(firstNode == None):
            foundEnd = True

    nodeToRemove = secondNode.link
    secondNode.link = nodeToRemove.link
    return head

def printLinkedList(head):
    foundEnd = False
    while not foundEnd:
        print(head.value)
        head = head.link
        if(head == None):
            foundEnd = True

main()
