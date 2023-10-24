P = int(input())
d1 = {}
d1['0'] = d1['O'] = d1['Q'] =  0
d1['1'] = d1['I'] = 1
d1['2'] = d1['Z'] = 2
d1['3'] = 3
d1['4'] = 4
d1['5'] = d1['S'] =  5
d1['6'] = 6
d1['7'] = 7
d1['8'] = 8
d1['9'] = 9
d1['A'] = 10
d1['C'] = d1['G'] = 11
d1['D'] = 12
d1['E'] = 13
d1['F'] = 14
d1['H'] = 15
d1['J'] = 16
d1['K'] = 17
d1['L'] = 18
d1['M'] = 19
d1['N'] = 20
d1['P'] = 21
d1['R'] = 22
d1['T'] = 23
d1['U'] = d1['V'] = d1['Y'] = 24
d1['W'] = 25
d1['X'] = 26

d2 = {}
for key, value in d1.items():
    d2[value] = key

for i in range(P):
    _, K = input().split()
    check = (2*d1[K[0]] + 4*d1[K[1]] + 5*d1[K[2]] + 7*d1[K[3]] + 8*d1[K[4]] + 10*d1[K[5]] + 11*d1[K[6]] + 13*d1[K[7]]) % 27
    if d2[check] == d2[d1[K[8]]]:
        decimal = d1[K[7]] + 27*d1[K[6]] + 27**2*d1[K[5]] + 27**3*d1[K[4]] + 27**4*d1[K[3]] + 27**5*d1[K[2]] + 27**6*d1[K[1]] + 27**7*d1[K[0]]
        print(_ + " " + str(decimal))
    else:
        print(_ + " Invalid")