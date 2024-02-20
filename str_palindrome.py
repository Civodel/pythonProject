

def is_palindrome(user_string:int):

    is_valid=False

    reversed_string=[]

    string_list= list(user_string)


    for index in range(len(string_list)):
        reversed_string.append(string_list[len(string_list)-1-index])

    if reversed_string== string_list:
        is_valid=True

    return is_valid




print(is_palindrome("aa"))