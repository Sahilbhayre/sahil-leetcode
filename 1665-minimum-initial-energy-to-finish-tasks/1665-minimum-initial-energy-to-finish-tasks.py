class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        total_energy = 0
        current_energy = 0

        for actual, minimum in tasks:
            if current_energy < minimum:
                needed = minimum - current_energy
                total_energy += needed
                current_energy += needed

            current_energy -= actual
        
        return total_energy