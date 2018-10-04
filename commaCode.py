def commaCode(list1):
    for item in range(len(list1) - 1):
        print(list1[item] + ',')
    print('and ' + list1[-1])


spam = ['apples', 'bananas', 'tofu', 'cats']

commaCode(spam)
