# [AUTHOR] user7141
# [DESCRIPTION] Python Clean solution
# [AUTHORS' NOTES] The intuition/ invariant is that self.top is always in the
#					First in Last out order, while self.stack is always in the
#					Last in First out order. This is analogous to the idea of
#					insertion sort where we have a sorted and unsorted portion.

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.top = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return -1
        if not self.top:
            while self.stack:
                self.top.append(self.stack.pop())
        return self.top.pop() 

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1 
        top = self.pop()
        self.top.append(top)
        return top

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.top and not self.stack

# ===================================================================================

# [AUTHOR] BalRavens55
# [DESCRIPTION] [Python] 2 Stacks O(1) Solution 98% Video Explanation
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        return ans

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.stack1 and not self.stack2)


# ===================================================================================

# [AUTHOR] xuhu357
# [DESCRIPTION] python3 intuitive solution
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        self.length += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.length <= 0:
            return None
        temp = self.stack1[0]

        self.stack2 = self.stack1[1:]
        self.stack1 = self.stack2

        self.length -= 1
        
        return temp


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.length <= 0:
            return None

        return self.stack1[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length == 0


# ===================================================================================

# [AUTHOR] pathak1515
# [DESCRIPTION] Python using Single Stack and List operations.

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.current_size = 0


    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        var = self.s1[0]
        self.s1.pop(0)
        return var


    def peek(self) -> int:
        if len(self.s1)<=0:
            return
        else:
            return self.s1[0]


    def empty(self) -> bool:
        if len(self.s1)==0:
            return True
        else:
            return False



# ===================================================================================

# [AUTHOR] Me
# [DESCRIPTION] First working solution
# [ISSUES]
#	Probably to most inefficient thing here is copying reverse array.
# [NOTES]
#	Maybe it will be better to have size property on an instance to
#	work with the indicies in a stack.
class MyQueue

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()
        self.reverseStack = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.reverseStack = self.stack[::-1] # copy in reverse order

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        queueHead = self.reverseStack.pop()
        self.stack = self.reverseStack[::-1]
        return queueHead

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.reverseStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack and self.reverseStack:
            return False

        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()