class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        result = []
        zero = 0

        for digit in nums:
            if digit != 0:
                total = total * digit
            else:
                zero += 1
        
        if zero > 1:
            return [0] * len(nums)

        for element in nums:
            if zero == 1 and element != 0:
                result.append(0)
            elif element != 0:
                result.append(int(total/element))
            else:
                result.append(total)
        return result