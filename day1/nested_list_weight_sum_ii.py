# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    
     def depthSumInverse(self, nestedList):
        """
        BFS
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        l1 = nestedList
        l2 = []
        sumEachLayer = []
        while True:
            s = 0
            for item in l1:
                if item.isInteger():
                    s += item.getInteger()
                else:
                    l2.extend(item.getList())
            sumEachLayer.append(s)
            if len(l2) == 0:
                break
            l1 = l2
            l2 = []
        
        sum2 = 0
        depth = 1
        for s in reversed(sumEachLayer):
            sum2 += depth * s
            depth += 1
        return sum2
