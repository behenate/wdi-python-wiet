from copy import deepcopy


def chess(t):
    def false_list(t):
        return [[False for _ in range(len(t))] for _ in
                range(len(t))]  # na tej tablicy będę zapamiętywał szachowane już pola

    # end

    def checked_sum_by_rook(t, i, j, checked_list):
        checked_sum = 0

        for k in range(len(t)):
            # jeśli pole nie było szachowane, oraz nie jest to pole na którym stała wierza początkowo
            if checked_list[i][k] == False and k != j:  # sumuję poziom k!=j omija pole na którym stała wieża
                checked_sum += t[i][k]
                checked_list[i][k] = True
            # end

            if checked_list[k][j] == False and k != i:  # sumuję pion
                checked_sum += t[k][j]
                checked_list[k][j] = True
            # end
        # end

        return checked_sum

    # end

    rook1 = (0, 0)  # pozycja wieży 1
    rook2 = (0, 0)  # pozycja wieży 2
    rook_biggest_sum = -1000000000  # zakładam że dane wejściowe będą większe

    for i in range(len(t)):
        for j in range(len(t)):
            rook1_checked = false_list(t)  # szkicuję tablicę do szachowania
            rook1_sum = checked_sum_by_rook(t, i, j,
                                            rook1_checked)  # referencja na tablicę sama nadpisuje szachowane pola

            for k in range(len(t)):
                for l in range(j, len(t)):  # żeby pominąć powtórki
                    rook2_checked = deepcopy(rook1_checked)  # deepcopy bo wiecej niż 1 mutable w strukturze
                    rook2_sum = checked_sum_by_rook(t, k, l, rook2_checked)

                    if rook_biggest_sum < rook1_sum + rook2_sum:  # aby nie użyć 2 razy tej samej wieży
                        rook1 = (i, j)
                        rook2 = (k, l)
                        rook_biggest_sum = rook1_sum + rook2_sum
                    # end
                # end
            # end
        # end
    # end

    return (rook1[0], rook1[1], rook2[0], rook2[1])