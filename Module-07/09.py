import result


def replace_word(s, replace_word):
    Answer = ""
    here_s = s.split(" ")
    for ind_j,j in enumerate(replace_with):
        for ind_i,i in enumerate(here_s):
            if i == j and ind_j % 2 == 0:
                here_s[ind_i]=replace_with[ind_j+1]
    for i in here_s:
        Answer+=i+" "
    return Answer

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

result = replace_word(s,replace_with)
print(result)
