
class Solution:


    def fibonacciSequence(self, nth_number: int):
        print(nth_number)
        if nth_number<0:
            print("incorrect input number there cant be negative")

        elif nth_number==0:
            return 0

        elif nth_number==1 or nth_number==2:
            return 1
        else:
            return self.fibonacciSequence(nth_number-1)+self.fibonacciSequence(nth_number-2)




fibonacci=Solution()

print(fibonacci.fibonacciSequence(10))