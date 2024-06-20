def extract_words_and_numbers(s):
    import re
    return [int(x) if x.isdigit() else x for x in re.findall(r'\d+|[a-zA-Z]+', s)]

input_string = "Nobody0expects42the2048Spanish1492Inquisition!"
result = extract_words_and_numbers(input_string)
print(result)


