class Solution(object):
    def averageValue(self, nums):
        div = []
        for num in nums:
            if num % 6 == 0:
                div.append(num)
        if div:
            return sum(div) / len(div)
        else:
            return 0