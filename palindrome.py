
# know what to do with the current integer


class Solution:
    def isPalindrome(self, integer:int):
        if integer < 0:
            return False

        reversed_num = 0
        temp = integer

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return True if reversed_num == integer  else False




palindrome= Solution()

print(palindrome.isPalindrome(985))