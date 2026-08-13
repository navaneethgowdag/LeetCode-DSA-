class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        # Map each number in nums1 to its index
        num1_idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            
            # While stack is not empty and current number is greater than top of stack
            while stack and cur > stack[-1]:
                val = stack.pop()
                # If the popped value is in nums1, update its result
                if val in num1_idx:
                    idx = num1_idx[val]
                    res[idx] = cur
            
            # Only push to stack if the current number is in nums1
            # (Optimization: we only care about numbers in nums1)
            if cur in num1_idx:
                stack.append(cur)
                
        return res   