# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
We will need to iterate the whole tree Root
We can use BFS to search for the first node of subroot, if we find the node,
we change to DFS to validate the trees are the same, if they are not we can
stop searching and continue with BFS
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is not None:
            return False
 
        if root is not None and subRoot is None:
            return True

        next_nodes = deque([root])

        while next_nodes:
            for _ in range(len(next_nodes)):
                node = next_nodes.popleft()

                if node.val == subRoot.val:
                    are_the_same = self.dfs(node, subRoot)
                    if are_the_same:
                        return True

                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
                
        return False

    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val == subRoot.val:
            left = self.dfs(root.left, subRoot.left)
            right = self.dfs(root.right, subRoot.right)
            return left and right

        return False