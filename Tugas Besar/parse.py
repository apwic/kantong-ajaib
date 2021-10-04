def parse(word,parser):

    temp = ""
    parse_value = []

    for char in word:
        if char == parser:
            parse_value.append(temp)
            temp = ""
        else:
            temp += char

    if temp:                             # Bernilai true kalo ga kosong
        parse_value.append(temp)

    return(parse_value)
