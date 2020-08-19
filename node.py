class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        str = ""
        while self:
            str += '%s->' % self.data
            self = self.next
        return str+'NULL'


list: ListNode = None
for i in range(1, 6):
    list = ListNode(i, list)
    pass

print("origin:", list)
