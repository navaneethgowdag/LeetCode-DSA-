class Solution(object):
    def averageValue(self, nums):
        div = []
        count = 0
        for num in nums:
            if num % 6 == 0:
                div.append(num)
                count += 1
        if div:
            return sum(div) / count
        else:
            return 0