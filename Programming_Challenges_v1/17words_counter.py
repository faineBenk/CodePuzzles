# lvl 1: using function


def word_counter(amount=0):
    for i in range(len(input().split())):
        amount += 1
    return amount


print(word_counter())
