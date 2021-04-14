my_file = open("fitness_hastags_clean", "r")
content = my_file.read()
print(content)

content_list = content.split(" ")
my_file.close()


print(content_list)

f = open("hastags_to_use.txt", "a")
f.write(str(content_list))
f.close()