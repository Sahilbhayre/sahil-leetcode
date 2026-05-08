class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        
        max_num = max(nums)
        
        # 1. Sieve to find the smallest prime factor (SPF) for each number
        spf = list(range(max_num + 1))
        for i in range(2, int(max_num**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # 2. Map each prime to indices where nums[j] is divisible by that prime
        prime_to_indices = {}
        for i, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = spf[temp]
                if p not in prime_to_indices:
                    prime_to_indices[p] = []
                prime_to_indices[p].append(i)
                while temp % p == 0:
                    temp //= p
        
        # 3. BFS
        queue = deque([(0, 0)]) # (current_index, distance)
        visited_indices = {0}
        visited_primes = set()
        
        # Helper to get prime factors of a number
        def get_prime_factors(num):
            factors = set()
            while num > 1:
                factors.add(spf[num])
                num //= spf[num]
            return factors

        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # Move 1: Adjacent Steps
            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    if neighbor == n - 1:
                        return dist + 1
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))
            
            # Move 2: Prime Teleportation (only if nums[curr_idx] is prime)
            # Checking if nums[curr_idx] is prime using our SPF array
            val = nums[curr_idx]
            if val > 1 and spf[val] == val:
                p = val
                if p not in visited_primes:
                    if p in prime_to_indices:
                        for next_idx in prime_to_indices[p]:
                            if next_idx not in visited_indices:
                                if next_idx == n - 1:
                                    return dist + 1
                                visited_indices.add(next_idx)
                                queue.append((next_idx, dist + 1))
                    visited_primes.add(p) # Mark prime as exhausted

        return -1