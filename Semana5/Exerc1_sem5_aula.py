fator = 2
while k % fator != 0 and fator <= k/2:
    fator = fator + 1
    if k % fator == 0:
        return False
    else:
        return k
