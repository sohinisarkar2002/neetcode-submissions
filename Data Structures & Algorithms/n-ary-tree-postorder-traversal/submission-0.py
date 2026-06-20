"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        postorder_list = []

        for child in root.children:
            postorder_list.extend(self.postorder(child))
        
        postorder_list.append(root.val)

        return postorder_list