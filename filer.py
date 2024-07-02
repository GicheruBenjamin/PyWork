
# Reading a file the usual way..
file = open('note.txt' , 'r')
c = file.read(); print(c) ; file.close()

# Using with statement
with open('note.txt' , 'r') as file:
    c = file.read()
    print(c)
