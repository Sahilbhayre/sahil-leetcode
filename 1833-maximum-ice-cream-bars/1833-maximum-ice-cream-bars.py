class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_cost = max(costs)

        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
        
        total_ice_creams = 0

        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
            
            if coins<cost:
                break
            
            affordable_count = min(freq[cost], coins // cost)

            total_ice_creams += affordable_count
            coins -= cost * affordable_count

        return total_ice_creams