


def non_repet(str1):
    for i in range(len(str1)):
        repeated = False
        for j in range(len(str1)):
            if str1[i] == str1[j] and i != j:
                repeated = True
                break
        if not repeated:
            return i
    return -1



s1 = "leetcode"
print(non_repet(s1))

