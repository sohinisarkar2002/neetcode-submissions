# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        st = [root]

        while st:
            curr = st.pop()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)
        
        return root



