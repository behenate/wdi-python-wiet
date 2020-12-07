
def to_binary(number, length):
    return format(number, 'b').zfill(length)


def apply_mask(mask, number):
    mask = str(mask)
    number = str(number)
    applied = ""
    for i, n in enumerate(mask):
        n = int(n)
        if n == 1:
            applied += number[i]

    if int(applied) % 7 == 0:
        print(applied)


def binary_mask_generator(number):
    length = len(str(number))
    top_mask_number = 2**length
    for i in range(1, top_mask_number):
        mask = to_binary(i, length)
        apply_mask(to_binary(i, length), number)


binary_mask_generator(2315)
