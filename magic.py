n = int(input())
if n < 4:
    print("число должно быть больше, либо равно 4")
    quit()
if n > 1000:
    print(("число должно быть меньше, либо равно 1000"))
    quit()
mat = [[0]*n for i in range(n)]
st, m = 1, 0
mat[n//2][n//2]=n*n
for v in range(n//2):
    for i in range(n-m):
        mat[v][i+v] = st
        st+=1
    for i in range(v+1, n-v):
        mat[i][-v-1] = st
        st+=1
    for i in range(v+1, n-v):
        mat[-v-1][-i-1] =st
        st+=1
    for i in range(v+1, n-(v+1)):
        mat[-i-1][v]=st
        st+=1
    m+=2
for i in mat:
    print(*i)