for i in range(200, 1000000):
    factor = 1
    sum_of_factors_i = 0
    while factor * factor <= i:
        if i % factor == 0:
            if i == factor * factor:
                sum_of_factors_i -= factor
            sum_of_factors_i += factor + (i // factor)
        factor += 1
    sum_of_factors_i -= i
    factor = 1
    sum_of_factors_j = 0
    while (factor * factor <= sum_of_factors_i) and (sum_of_factors_i < i):
        if sum_of_factors_i % factor == 0:
            if sum_of_factors_i == factor * factor:
                sum_of_factors_j -= factor
            sum_of_factors_j += factor + (sum_of_factors_i // factor)
        factor += 1
    sum_of_factors_j -= sum_of_factors_i
    if sum_of_factors_j == i:
        print(i, sum_of_factors_i)