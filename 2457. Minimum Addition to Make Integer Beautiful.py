class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        def get_digit(i, num):
            return num % (10**(i + 1)) // (10**i)

        def get_digits_sum(num):
            digits_sum = 0
            while num > 0:
                digits_sum += num % 10
                num //= 10
                
            return digits_sum

        i, new_n = 0, n
        while get_digits_sum(new_n) > target:
            new_n += (10 - get_digit(i, new_n)) * (10**i)
            i += 1

        return new_n - n