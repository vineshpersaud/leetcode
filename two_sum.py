 def twoSum(self, nums: List[int], target: int) -> List[int]:

        array = []
        for  idx, num in enumerate(nums):
            for  idx2, num2 in enumerate(nums):
                if num + num2 == target and idx != idx2:
                    return([idx,idx2])

                    
