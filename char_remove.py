special_char = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

sentence = "i a!!#m a s[)(oftw<>ar$%^&*e en\/?g~in-eer"

s = ""
for char in sentence:
    if char not in special_char:
        s = s + char

print(s)