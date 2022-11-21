def replace_comma_with_space(text):
    new_text = ' '.join(i for i in text.split(','))
    return new_text

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)

