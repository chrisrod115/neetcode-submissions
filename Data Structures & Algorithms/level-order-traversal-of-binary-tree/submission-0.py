# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q, res = deque([root]), []
        while q:
            cur, n = [], len(q)
            for _ in range(n):
                n1 = q.popleft()
                cur.append(n1.val)
                if n1.left:
                    q.append(n1.left)
                if n1.right:
                    q.append(n1.right)
            res.append(cur)
        return res