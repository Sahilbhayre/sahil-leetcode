class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        m = len(s)
        
        # 1. Extract non-zero digits and track their original indices
        nonzero_vals = []
        nonzero_indices = []
        for i in range(m):
            if s[i] != '0':
                nonzero_vals.append(int(s[i]))
                nonzero_indices.append(i)
                
        n = len(nonzero_vals)
        
        # If there are no non-zero digits, all queries yield 0
        if n == 0:
            return [0] * len(queries)
            
        # 2. Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        # 3. Prefix sum of individual digits
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nonzero_vals[i]
            
        # 4. Prefix evaluation of the concatenated values
        pref_val = [0] * (n + 1)
        for i in range(n):
            pref_val[i+1] = (pref_val[i] * 10 + nonzero_vals[i]) % MOD
            
        # 5. Build lookup maps for fast range mapping
        nxt = [n] * m
        idx = 0
        for i in range(m):
            while idx < n and nonzero_indices[idx] < i:
                idx += 1
            nxt[i] = idx
            
        prv = [-1] * m
        idx = n - 1
        for i in range(m - 1, -1, -1):
            while idx >= 0 and nonzero_indices[idx] > i:
                idx -= 1
            prv[i] = idx

        # 6. Process each query in O(1) time
        ans = []
        for l, r in queries:
            i_start = nxt[l]
            i_end = prv[r]
            
            # If there are no non-zero elements in the range [l, r]
            if i_start > i_end:
                ans.append(0)
                continue
                
            # Compute digit sum using prefix array
            digit_sum = pref_sum[i_end + 1] - pref_sum[i_start]
            
            # Extract the slice number modulo MOD
            length = i_end - i_start + 1
            x = (pref_val[i_end + 1] - pref_val[i_start] * pow10[length]) % MOD
            
            # Append final product modulo MOD
            ans.append((x * digit_sum) % MOD)
            
        return ans