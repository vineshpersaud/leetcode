# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        numList = []
        currentNode1 = l1
        currentNode2 = l2

        while currentNode1:
            numList.append(currentNode1.val)
            currentNode1 = currentNode1.next
        while currentNode2:
            numList.append(currentNode2.val)
            currentNode2 = currentNode2.next

        numList.sort()

        newNode = None
        lastNewNode = None

        for node in numList :
            if newNode == None:
                newNode = ListNode(node)
                lastNewNode = newNode
            else :
                lastNewNode.next = ListNode(node)
                lastNewNode = lastNewNode.next

        return newNode
