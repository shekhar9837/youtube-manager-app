
# first way 


# file = open('youtube.txt', 'w')
# try:
#     file.write("hello first word")
# finally:
#     file.close()



# second way
with open('youtube.txt', 'w') as file:
    file.write("hello second word")

