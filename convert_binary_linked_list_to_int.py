class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        currentNode = head
        nodeList = []
        nextNode = True
        while nextNode:
            nodeList.append(str(currentNode.val))
            if currentNode.next == None:
                nextNode = False
            else:
                currentNode = currentNode.next
        binary = ''.join(nodeList)
        return int((binary),2)