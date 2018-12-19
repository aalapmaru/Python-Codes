
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node,leftnode,rightnode):
            if node is None:
                return True
            if leftnode is not None and node.val<=leftnode  or rightnode is not None and node.val>=rightnode :
                return False
            
            
            return valid(node.left,leftnode,node.val) and valid(node.right,node.val,rightnode)
        
        return valid(root,None,None)
