# Breadth first search


# Time Complexity : O(n)
# space complexity : O(n)

# Approach :

# use bfs
# check the last element for each level
# keep appending in the list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.q = deque()
        self.listVal = []
        self.bfs(root)
        return self.listVal

    def bfs(self, root):

        self.q.append(root)
        while self.q:

            size = len(self.q)
            for i in range(0, size):
                poppedVal = self.q.popleft()
                if poppedVal:
                    if i == size-1:
                        self.listVal.append(poppedVal.val)
                    if poppedVal.left is not None:
                        self.q.append(poppedVal.left)
                    if poppedVal.right is not None:
                        self.q.append(poppedVal.right)


# Depth first search


# Time Complexity : O(n)
# space complexity : O(h)

# Approach :

# use dfs
# check if level is equal to the len(list)
# first traverse root.right
# second traverse root.left


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, level):

        if not root:
            return None

        if len(self.result) == level:
            self.result.append(root.val)

        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)
