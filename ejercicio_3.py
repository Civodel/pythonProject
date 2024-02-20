class Solution:
    def not_double_zero(self,*params):
        const="00"
        new_word= "".join(str(word) for word in params)
        return True if const in new_word else False


double_zero =  Solution()

print(double_zero.not_double_zero(10,1,2,3,4,5,0,0))