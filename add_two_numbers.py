class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = [l1]
        list2 = [l2]

        while (list1[0].next):
            list1.insert(0,(list1[0].next))

        num1 = ''.join(list(map((lambda num: str(num.val)) , list1)))

        while (list2[0].next):
            list2.insert(0,(list2[0].next))

        num2 = ''.join(list(map((lambda num: str(num.val)) , list2)))


        sum = list(str(int(num1)+int(num2)))
        sum = sum[::-1]
        sumInt = list(map((lambda num: int(num)), sum))

        node = None
        currentNode = None

        for num in sumInt :
            if (currentNode == None):
                node = ListNode(num)
                currentNode = node
            else :
                currentNode.next = ListNode(num)
                currentNode = currentNode.next

        return node
