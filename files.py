text_file = open("file1.txt")
text_file_2= open("file2.txt")



first_file=text_file.read()
second_file=text_file_2.read()


unique_chars=[]

for line in first_file:
    if line not in second_file:
        unique_chars.append(line)

print(unique_chars)


text_file.close()
text_file_2.close()