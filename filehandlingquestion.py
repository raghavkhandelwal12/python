#python program to read file word by word
with open('gfg.txt','r')as file:
    #reading each line
    for line in file:
        for word in line.split():
            print(word)