class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) is (divisor > 0)
        divisor, dividend = abs(divisor), abs(dividend)

        frac = 0
        the_sum = divisor

        while the_sum <= dividend:
            curr_frac = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                curr_frac += curr_frac
            dividend -= the_sum
            the_sum = divisor
            frac += curr_frac

        return min(2147483647, max(frac if positive else -frac, -2147483648))