##********************using while lopp***************************
class TrapWater:
    def trap_water(self,height:list[int]):
        if not height:
            return 0
        l,r = 0,len(height)-1
        leftMaxArray=height[l]
        rightMaxArray= height[r]
        result = 0

        while l<r:
            if leftMaxArray < rightMaxArray:
                l+=1
                leftMaxArray = max(leftMaxArray,height[l])
                result+=leftMaxArray-height[l]
            else:
                r-=1
                rightMaxArray =max(rightMaxArray,height[r])
                result+=rightMaxArray-height[r]
        return result

height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap_water = TrapWater()
print(trap_water.trap_water(height))

##********************using for loop ***************************
class TrapWater:
    def trap_water(self, height: list[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        result = 0

        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate the total water trapped
        for i in range(n):
            result += min(left_max[i], right_max[i]) - height[i]
        
        return result

# Test the function
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trap_water = TrapWater()
print(trap_water.trap_water(height))
