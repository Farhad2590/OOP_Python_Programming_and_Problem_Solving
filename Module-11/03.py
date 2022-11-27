s = "Programming Hero is the best"

word = s.split(" ")

new_word = [i[::-1]for i in word]

new_string= " ".join(new_word)

print(new_string)