#main() contains test cases for the serialize and deserialize methods
#The first test is to make sure their assert can be passed and the second test
#is a custom tree I built based on the image I included. It shows the serialized array,
#then deserializes it into a tree again, then serializes it again to show they give
#the same results.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    #Test1:
    test1Node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(test1Node)).left.left.val == 'left.left'
    
    #Test2:
    node = Node(5, Node(3, Node(1, None, Node(2)), Node(4)), Node(8, Node(7), Node(9)))

    serializedNode = serialize(node)
    print("Serialized:   " + serializedNode)

    deserializedNode = deserialize(serializedNode)
    reserializedNode = serialize(deserializedNode)
    print("Reserialized: " + reserializedNode)

    
def serialize(node):
    serializedNode = serializeHelper(node)[:-1]
    return serializedNode
    

def serializeHelper(node):
    if(node == None):
        return 'x,'
    
    serializedNode = str(node.val) + ',' + serializeHelper(node.left) + serializeHelper(node.right)

    return serializedNode

def deserialize(serializedNode):
    values = serializedNode.split(',')
    nextIndex = 0
    
    leftBranch = deserializeHelper(values, 1)
    leftNode = leftBranch[0]
    nextIndex = leftBranch[1]
    
    rightBranch = deserializeHelper(values, nextIndex)
    rightNode = rightBranch[0]
    
    return Node(values[0], leftNode, rightNode)

def deserializeHelper(array, index):
    if(array[index] == 'x'):
        index += 1
        return [None, index]

    value = array[index]
    index += 1
    
    leftBranch = deserializeHelper(array, index)
    leftNode = leftBranch[0]
    index = leftBranch[1]
    
    rightBranch = deserializeHelper(array, index)
    rightNode = rightBranch[0]
    index = rightBranch[1]

    return [Node(value, leftNode, rightNode), index]

main()
