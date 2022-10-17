print(str(
[i for i in range(3)]
))

l = []
for i in range(3):
    for j in range(3):
        l.append(i)

print(l)

d = {
    '0': "A",
    "1": "B"
}

p = ["P", "J", "Ju"]

for k,v in enumerate(p):
    print(str(k) + " " + str(v))

dico = {k:v for k, v in enumerate(p)}
print(dico)

