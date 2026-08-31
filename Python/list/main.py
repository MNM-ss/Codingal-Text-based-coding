empty_list = [print()]
print()
num = [1, 2, 3]
print(num)

triple = [1, 2, 3]*3
print(triple)

alist = [100, 200, 300, 400, 500]
alist = alist[::-1]
print(alist, "\n")



def match_words (words):
    ctr = 0
    lst = []
    for word in words:
     if len(word) > 1 and word [0] == word[-1]:
        ctr += 1
        lst.append(word)
    print("List of words with first and last character same\n", lst)
    return ctr
count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count)