# Depth first search


# Time Complexity : O(n)

# space complexity : O(h)

# Approach :

# use dfs
#  keep track of level and xparent, yparent, xlevel and ylevel
#  check if xlevel and ylevel are same but the parents are different


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xLevel = 0
        self.yLevel = 0
        self.xParent = None
        self.yParent = None

        self.dfs(root, None, x, y, 0)

        if self.xParent != self.yParent and self.xLevel == self.yLevel:
            return True
        else:
            return False

    def dfs(self, root, parent, x, y, level):

        if root is None:
            return None

        if root.val == x:
            self.xParent = parent
            self.xLevel = level+1

        if root.val == y:
            self.yParent = parent
            self.yLevel = level+1

        self.dfs(root.left, root, x, y, level+1)
        self.dfs(root.right, root, x, y, level+1)


# Breadth first search


# Time Complexity : O(n)

# space complexity : O(n)


# Approach :

# use bfs
#  first check if root.val is equal to x or y
#  then check if root has two children, if it does, check if x and y are its children, if so return false
#  after every level, we keep a check if xfound and yfound is true, if so return true
# if either one is true and the other is false, return false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if not root:
            return False

        self.q = deque()
        result = self.bfs(root, x, y)
        return result

    def bfs(self, root, x, y):

        xFound = False
        yFound = False
        self.q.append(root)

        while self.q:

            size = len(self.q)

            for i in range(0, size):

                poppedVal = self.q.popleft()

                if poppedVal.val == x:
                    xFound = True
                if poppedVal.val == y:
                    yFound = True

                if poppedVal.left is not None and poppedVal.right is not None:

                    if poppedVal.left.val == x and poppedVal.right.val == y:
                        return False

                    if poppedVal.left.val == y and poppedVal.right.val == x:
                        return False

                if poppedVal.left:
                    self.q.append(poppedVal.left)
                if poppedVal.right:
                    self.q.append(poppedVal.right)

            if xFound == True and yFound == True:
                return True

            if xFound == True or yFound == True:
                return False

        return False
