# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp=0
        output = []
        while True:
            if l1 != None:
                v1 = l1.val
            else:
                v1=0
            if l2 != None:
                v2 = l2.val
            else:
                v2=0
            num_sum = tmp+v1+v2
            num_str = str(num_sum)
            output.append(int(num_str[-1]))
            if len(num_str)==2:
                tmp=int(num_str[0])
            else:
                tmp=0
            if l1 !=None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            if l1 == None and l2 ==None:
                break
        if tmp!=0:
            output.append(tmp)
        N = len(output)
        node  =  ListNode(output[N - 1],None)
        for i in range(N-1):
            node = ListNode(output[N-2-i],node)
        return node

if __name__ == '__main__':
    str = "214"
