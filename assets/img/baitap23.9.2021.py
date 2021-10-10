List = []
print("Nhập ma nhận mxn")
m=int(input("Nhap gia tri m:"))
n=int(input("Nhap gia tri n:"))
for i in range(m):
    List.append([])
    for j in range(n):
        List[i].append(0.0)
ListNew=[]
while True:
    nhapi=int(input("Nhap gia tri i voi 0<=i<"+str(m)+":"))
    nhapj=int(input("Nhap gia tri j voi 0<=j<"+str(n)+":"))
    if 0<=nhapi<m and 0<=nhapj<n:
        break
nhapgt=int(input("Nhap gia tri moi:"))
for i in range(m):
    ListNew.append([])
    for j in range(n):
        if nhapi==i and nhapj==j:
            ListNew[i].append(nhapgt)
        else:
            ListNew[i].append(0)
print(ListNew)