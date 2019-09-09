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
block=int(input("jumlah block :"))
cek=input("input plain text : ").upper()
hasil=""
c=0
key=kunci[c]
count=0
for i in range(len(cek)):
    if count==block:
        c+=1
        if c>=len(kunci):
            c=c%len(kunci)
        key=kunci[c]
        count=0
    hasil+=key[plain.index(cek[i])]
    count+=1
print(hasil)
