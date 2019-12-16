class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        topBottom = []
        leftRight = []
        
        # skyline viewed from left or right max
        for girdList in grid :
            leftRight.append(max(girdList))
        
        # skyline viewed from top or bottom max
        for i in range(len(grid[0])):
            currentList = []
            for girdList in grid :
                currentList.append(girdList.pop(0))
            topBottom.append(max(currentList))
