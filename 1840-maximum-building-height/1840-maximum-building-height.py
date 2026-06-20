class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])
        restrictions.append([n, n-1])

        restrictions.sort()
        m = len(restrictions)

        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + dist)

        for i in range(m - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + dist)

        max_height = 0

        for i in range(1, m):
            l_id, l_h = restrictions[i - 1]
            r_id, r_h = restrictions[i]

            peak = (r_id - l_id + l_h + r_h) // 2
            max_height = max(max_height, peak)

        return max_height