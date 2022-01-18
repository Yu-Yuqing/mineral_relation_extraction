import re

with open("2.txt", 'r', encoding='utf-8') as f:
        file = ""
        pattern = re.compile(r'	')
        for number,line in enumerate(f,start=1):
            if (len(pattern.findall(line))) == 7:
                file += line
            # if len(re.compile("	")) != 7:
            #     print(number)
with open("3.txt", "w" ,encoding='utf-8') as f:
    f.write(file)
f.close()




