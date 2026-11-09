"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        node_dict, queue = {node:Node(node.val)}, deque([node])
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in node_dict:
                    node_dict[neighbor] = Node(neighbor.val)
                    queue.append(neighbor) 
                node_dict[current_node].neighbors.append(node_dict[neighbor])

        return node_dict[node]
