with open("new.txt", 'r', encoding='utf-8') as f:
        file = ""
        for number,line in enumerate(f,start=1):
            # print(line[0:3])
            if line[0:4] == "(\"('":
                file += line
with open("2.txt", "w" ,encoding='utf-8') as f:
    f.write(file)
f.close()



