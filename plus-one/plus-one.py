class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] != 9:
                    digits[i] += 1
                    break
                digits[i] = 0
            if i == 0 and digits[0] == 0:
                digits[0] = 1
                digits.append(0)
        else:
            digits[-1] += 1
        return digits