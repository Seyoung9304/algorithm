a = list(input())
op = input()
b = list(input())

la, lb = len(a), len(b)

if op=="*":
    print("1"+"0"*(la+lb-2))
else:
    if la < lb:
        b[-la] = ('1' if b[-la]=='0' else '2')
        print(''.join(b))
    else:
        a[-lb] = ('1' if a[-lb]=='0' else '2')
        print(''.join(a))