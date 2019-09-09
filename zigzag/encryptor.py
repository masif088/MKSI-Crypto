def keygen():
    plain="ABCDEFGHIJKLMNOPQRSTQUVWXYZ"
    key=input("input kunci :").upper()
    for i in plain:
        for j in range(len(key)):
            if key[j]==i:
                break
            if j==len(key)-1:
                key+=i
    return key
jumlahkunci=int(input("jumlah kunci : "))
kunci=[None]*jumlahkunci
for i in range (jumlahkunci):
    kunci[i]=keygen()
plain="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cek=input("input plain text : ").upper()
hasil=""
temp=""
for j in range (jumlahkunci):
    if j==0:
        for i in range(26):
            hasil+=kunci[j][plain.index(plain[i])]
        temp=hasil
        hasil=""
    else:
        for i in range(26):
            hasil+=plain[kunci[j].index(temp[i])]
        temp=hasil
        hasil=""
for i in range (len(cek)):
    hasil+=plain[temp.index(cek[i])]
print(hasil)
