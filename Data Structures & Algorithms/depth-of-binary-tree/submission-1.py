# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        cnt = 0
        # left, right = 0, 0

        # while st:
        #     curr = st.pop()

        #     if curr.left:
        #         st.append(curr.left)
        #         left += 1
        #     if curr.right:
        #         st.append(curr.right)
        #         right += 1

        # cnt += max(left, right)

        while q:
            l = len(q)

            for _ in range(l):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            cnt += 1

        return cnt