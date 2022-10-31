strg = "Only when it comes to money. My life is a different story. Im still alive arent I?"

# type and lenght
print(type(strg))
print(len(strg))

# Replaces a substring with something else.
s1 = print(strg.replace("Only", "Just"))

# The string starts with? bool
print(strg.startswith("Only"))

# The string ends with? bool
print(strg.endswith("T"))

# how many occurrences
print(strg.count("."))

# substrings
print(strg[0])
print(strg[1:8])
print(strg[4:])
print(strg[::2])  # even
print(strg[1::2])  # odd
print(strg[::-1])  # reverse
