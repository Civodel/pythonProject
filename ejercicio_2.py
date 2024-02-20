class   Solution():
    def devolver_caracteres_unicos(self,user_string:str )->list:
        unique_chars=set()

        for letter in user_string:
            if letter not in unique_chars:
                unique_chars.append(letter)
        unique_chars.sort()
        return unique_chars



caracteres_unicos = Solution()

word=input("Please enter")

print(caracteres_unicos.devolver_caracteres_unicos(word))