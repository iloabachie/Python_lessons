import string


def autocorrect(text: str) -> str:
    list_of_words = text.split()
    # print(list_of_words)
    for index in range(len(list_of_words)):
        temp = mark = ""
        if list_of_words[index][-1].lower() not in string.ascii_lowercase:
            mark = list_of_words[index][-1]
            temp = list_of_words[index][:-1]
        else:
            temp = list_of_words[index]
        if temp.lower() in ["u", "you"]:
            list_of_words[index] = "your client" + mark
        elif temp[:3].lower() == "you" and set(temp[3:]) == {"u"}:
            list_of_words[index] = "your client" + mark
    # print(" ".join(list_of_words))
    return " ".join(list_of_words)


msg = "you are not  u ready for me.  youuu. arent ready green u"


print(autocorrect(msg))