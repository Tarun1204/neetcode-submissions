"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        cloned = {}
        
        # This check is useless (cloned is empty at this point)
        if node.val in cloned:
            return cloned[node.val]
        
        def helper(node):
            # Create a new node
            newN = Node(node.val)
            
            # Store it using its VALUE as key (NOT object reference)
            cloned[node.val] = newN

            # Visit all neighbors
            for child in node.neighbors:
                # Check if this neighbor's VALUE was already cloned
                if child.val in cloned:
                    childClone = cloned[child.val]
                else:
                    childClone = helper(child)
                
                # Connect the cloned neighbor
                newN.neighbors.append(childClone)
            
            return newN
        
        return helper(node)
        