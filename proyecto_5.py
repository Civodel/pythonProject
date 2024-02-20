import random
import math
import re

class Game():
    def __init__(self,vida_jugador):
            self.vida_jugador=vida_jugador

    def pick_word(self):
        word_set=["bazinga","batman","superman","bigfoot","dinosautio"]
        word=random.choice(word_set)



        return word
    def validate_input(self, user_input):
        regex="^[0-9,$]*$"

        validate_input=re.search(regex,user_input)

        while validate_input:
            print("Invalid input try again")
            user_input=input("hola")
            validate_input = re.search(regex, user_input)

        else:
            return user_input.lower()
    def encripted_word(self,choice_word):
        encode_word=""
        for letter in choice_word:
            encode_word+="_"

        return encode_word
    def letter_in_word(self,word, user_input, encode_word):

        word_list = list(word)
        encode_word_list =list(encode_word)
        fail=True

        while user_input in word_list:
          index = word_list.index(user_input)
          encode_word_list[index] = user_input
          word_list[index]="*"
          fail=False

        encode_word="".join(encode_word_list)
        return encode_word,fail

    def game_over(self,player_hp):
        if player_hp<=0:
            return True
        else:
            return False

    def game_out(self):
        self.vida_jugador =self.vida_jugador -1

    def game_win(self,word):
        if "_" not in word:

            return True
        else:
            return False



    def hanging_three_main(self):
        print("Welcome to the game MF")
        name_player =input("ingresa tu nombre owo \n ")
        print(f"Bienvenido {name_player} al juego del ahorcado:\n")
        word=self.pick_word()
        choisen_word=self.encripted_word(word)

        while self.game_over(self.vida_jugador) == False:


            print(f"Vidas Restantes: {self.vida_jugador}")
            print(f"{choisen_word}")

            user_input=input("Ingresa Una Letra BB: \n")

            validated_user_input=self.validate_input(user_input)
            choisen_word,fail=( self.letter_in_word(word,validated_user_input,choisen_word))
            if fail == True:
                self.game_out()

            if self.game_win(choisen_word) == True:
                print(f"Has Ganado {name_player}")
                break
        else:
            print(f"Has Perdido {name_player}")
            print(f"La palabra era {word}")





        return ("Buen Juego <3")



juego_1=Game(10)
print(juego_1.hanging_three_main())




