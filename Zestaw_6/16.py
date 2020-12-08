vowels = {"a", "e", "i", "o", "u"}


def can_build(s1, s2):
    s1_vowels = 0
    s1_ascii = 0
    for letter in s1:
        if letter in vowels:
            s1_vowels += 1
        s1_ascii += ord(letter)

    def build(index=0, combination="", c_vowels=0, c_ascii=0):
        print(combination)
        if s1_ascii == c_ascii and s1_vowels == c_vowels:
            return True
        if index == len(s2) or c_vowels > s1_vowels or c_ascii > s1_ascii:
            return False
        to_ret = False
        for i in range(index, len(s2)):
            vowel = 1 if s2[i] in vowels else 0
            to_ret = to_ret or build(i+1, combination+s2[i], c_vowels+vowel, c_ascii+ord(s2[i]))
        return to_ret
    return build()

print(can_build("ula", "exe"))