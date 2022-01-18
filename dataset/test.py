with open("test.txt", 'r', encoding='utf-8') as f:
        file = ""
        for number,line in enumerate(f,start=1):
            if line != "\n":
                if len(line)!=4:
                    line = line[0:4]+"\n"+"\n"+line[4:]
            file += line
with open("2.txt", "w" ,encoding='utf-8') as f:
    f.write(file)
f.close()
