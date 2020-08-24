arr=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j], arr[j][i]==arr[j][i], arr[i][j]

#zip(iterable*)
alpha=['a','b','c']
index=[1,2,3]
alpha_index=list(zip(alpha, index))
print(alpha_index) #[('a',1),('b',2),('c',3)]
#따라서, 전치 행렬을 zip함수를 이용해 만들 수 있음(아래)
print(list(zip(*arr)))
