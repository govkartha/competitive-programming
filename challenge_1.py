n = int(input())
val = map(int,input().split())
word = input().split()

pairs = list(zip(val,word))
limit = 100

for i in range(1,limit+1):
    op = ''
    for v,w in pairs:
        if i%v == 0:
            op +=w
    
    print(i if op == '' else op, end = " ")