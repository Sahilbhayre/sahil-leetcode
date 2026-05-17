class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        queue = deque([start])

        while queue:
            curr = queue.popleft()

            if arr[curr] == 0:
                return True

            if arr[curr] < 0:
                continue

        
            jump = arr[curr]
            arr[curr] =- arr[curr]

            for next_idx in (curr + jump, curr - jump):
                if 0 <= next_idx < len(arr) and arr[next_idx] >= 0:
                    queue.append(next_idx)


        return False