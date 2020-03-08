fp=open("Book1", "r")
fp2=open("Book2", "w")
list=[]
fp_content= fp.read()
punct= "ª!·.,-_:;$%&/()=?¿^"
line= " "
for p in fp_content:
    if p not in punct:
        line= line + p
for x in line:
    if x not in list:
        list.append(x)
        fp2.write(str(x)+"\n")
print(len(list))

