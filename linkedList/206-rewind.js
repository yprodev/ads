/*
# [AUTHOR] Ravikanth
# [DESCRIPTION] Simple python iterative solution
def reverseList(self, head):
        first = head
        current = None
        previous = None
        while first:
            current = first
            first = first.next
            current.next = previous
            previous = current
        return current


def reverseList(self, head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev



===================================================================================



    [AUTHOR] Me (Copied Python3 solution from Ravikanth)
    [DESCRIPTION] REWIND in JavaScript
    [ISSUES]
        1. Basic knowledge in Python 3.
        2. Issues with the last node ---> issues with understanding that while loop is stopped
        on the one item before the last one.
        3. Issues with submition because of another edge case.
*/

let reverseList = function(head) {

    let first = head;
    let current = null;
    let previous = null;
    
    while (!!first) {
        current = first;
        first = first.next;
        current.next = previous;
        previous = current;
    }
    
    return previous;
    
};

