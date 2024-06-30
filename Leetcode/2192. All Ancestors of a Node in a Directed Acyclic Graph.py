class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        # Determine children nodes and root node and initialize ancestors of all nodes
        children = {}
        ind = [0] * n
        ancestors = []
        for i in range(n):
            children[i] = []
            ancestors.append([])

        for edge in edges:
            children[edge[0]].append(edge[1])
            ind[edge[1]] += 1
        
        # Determine the root nodes and add to a queue
        from collections import deque
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)

        
        # Define a merger function for merging the ancestors of two parents properly
        def merger(list1, list2):
            ans = []
            i = 0
            j = 0

            while i < len(list1) and j < len(list2):
                if list2 and list1[i] > list2[-1]:
                    return ans + list2[j:] + list1[i:]
                if list1 and list2[j] > list1[-1]:
                    return ans + list1[i:] + list2[j:]

                if list1[i] < list2[j]:
                    ans.append(list1[i])
                    i += 1
                elif list1[i] > list2[j]:
                    ans.append(list2[j])
                    j += 1
                else:
                    ans.append(list1[i])
                    i += 1
                    j += 1
            
            if i < len(list1):
                ans += list1[i:]
            elif j < len(list2):
                ans += list2[j:]
            
            return ans
        
        # Implement BFS from root nodes and store all parent nodes for each node
        # only add children when they have no parents
        while len(q) != 0:
            node = q.popleft()
            for child in children[node]:
                ancestors[child] = merger(ancestors[child], [node])
                ancestors[child] = merger(ancestors[child], ancestors[node])
                ind[child] -= 1
                if ind[child] == 0:
                    q.append(child)
        
        return ancestors