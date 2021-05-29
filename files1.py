with open("referat.txt", 'r', encoding = "utf-8") as referat:

    text = referat.read()
    print(text)
    
    words = text.split()
    wordcount = len(words)
    print(f"Количество слов: {wordcount}")
    print(f"Длина строки или количество символов: {len(text)}")

    new_text = text.replace(".", "!")
    print(new_text)
    
with open("referat2.txt", 'a', encoding= 'utf-8') as referat2:
    referat2.write(new_text)
    referat2.close()    