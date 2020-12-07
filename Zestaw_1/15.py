#Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
# sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π
#
# pi = 2/sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5))) ∗ ...

from math import *
import time
pi = 0
p_pi = 1
res = sqrt(0.5)
prev = res

while p_pi != pi:
    p_pi = pi
    prev = sqrt(0.5 + (0.5 * prev))
    res = res*prev
    pi = 2/res
print(pi)
