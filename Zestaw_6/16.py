vowels = {"a", "e", "i", "o", "u"}


def can_build(s1, s2):
    s1_vowels = 0
    s1_ascii = 0
    for letter in s1:
        if letter in vowels:
            s1_vowels += 1
        s1_ascii += ord(letter)
    available_indexes = [i for i in range(len(s2))]

    def build(a_i, combination="", c_vowels=0, c_ascii=0):
        if s1_ascii == c_ascii and s1_vowels == c_vowels:
            return True
        if len(a_i) == 0 or c_vowels > s1_vowels or c_ascii > s1_ascii:
            return False

        to_ret = False
        for elem in a_i:
            a = [""]*(len(a_i)-1)
            cnt = 0
            for elem1 in a_i:
                if elem1 != elem:
                    a[cnt] = elem1
                    cnt += 1
            vowel = 1 if s2[elem] in vowels else 0
            to_ret = to_ret or build(a, combination+s2[elem], c_vowels+vowel, c_ascii+ord(s2[elem]))
        return to_ret
    return build(available_indexes)


print(can_build("ula", "exe"))