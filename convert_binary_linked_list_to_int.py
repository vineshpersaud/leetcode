class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        currentNode = head
        nodeList = []
        while currentNode:
            nodeList.append(str(currentNode.val))
            currentNode = currentNode.next
        binary = ''.join(nodeList)
        return int((binary),2)