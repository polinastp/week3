with open('myfile.txt' ,'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.upper()
        line = line.replace("\n", "")
        print(line)