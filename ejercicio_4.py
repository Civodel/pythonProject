class Solution:
    def contar_primos(self, number:int):
        for num in range(2,number):
            if number % num == 0:
                return False
        print("primo")



        return True



primos= Solution()

print(primos.contar_primos(5))