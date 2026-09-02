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

L=[4, 5, 1, 2, 9, 7, 10, 8]
print("original List:", L)

count = 0
for i in L:
    count += i

avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])

