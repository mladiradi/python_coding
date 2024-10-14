
import re

text = input()
emoji_pattern = r'(\:\:[A-Z][a-z]{2,}\:\:)|(\*\*[A-Z][a-z]{2,}\*\*)'
digit_pattern = r'\d'
emojis = re.findall(emoji_pattern, text)
digits = re.findall(digit_pattern, text)
cool_threshold = 1
valid_emojis = []

for digit in digits:
    cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")

# emoji = emoji_pair[0] if emoji_pair[0] else emoji_pair[1]
for emo in emojis:
    if emo[0]:
        emoji = emo[0]
    else:
        emoji = emo[1]
    emoji_coolness = 0

# emoji_coolness = sum(ord(char) for char in emoji if char.isalpha())
    for char in emoji:
        if char.isalpha():
            emoji_coolness += ord(char)

    if emoji_coolness > cool_threshold:
        valid_emojis.append(emoji)

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    print(emoji)

# # input:
#
# In the Sofia Zoo there are 311 animals in total! ::Smiley::
# This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**,
# a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::.
# ::Mooning:: **Shy**

# # output:
#
# Cool threshold: 540
# 4 emojis found in the text. The cool ones are:
# ::Smiley::
# **Tigers**
# ::Mooning::
