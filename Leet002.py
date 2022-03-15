def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        itr = ans
        carryOver = 0
        while l1 is not None or l2 is not None:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            itr.val = num1 + num2 + carryOver
            carryOver = 0
            if itr.val > 9:
                carryOver = 1
                itr.val -= 10
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            if l1 or l2:
                itr.next = ListNode()
                itr = itr.next
        if carryOver:
            itr.next = ListNode(carryOver)
        return ans