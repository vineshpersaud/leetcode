class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, str(n)))
        product = 1
        for num in nums :
            product = num * product
        return product - sum(nums)
        