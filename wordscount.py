import operator
fbook = input("Text2_clean")
dict_of_words = {}
with open(fbook, 'r', encoding="utf8") as fhand:
    for line in fhand:
        line.strip()
        new_line = ''.join(c for c in line if c.isalnum() or c == "’" or c ==' ' or c == '—' or c =='-')
        new_line = new_line.replace("—"," ")
        words_of_line = new_line.split()
        for word in words_of_line:
            if word[-1] == '’':
                word = word[:len(word)-1]
            word = word.lower()
            if word not in dict_of_words.keys():
                dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1
    sorted_list_of_words = sorted(dict_of_words.items(), key=operator.itemgetter(1), reverse=True)
    print("{:<20} {:<}".format("Word", "Frequency"))
    for w,f in sorted_list_of_words:
        print("{:<20} {:<}".format(w,f))

