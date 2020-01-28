# coding:utf-8
# Travail fait par Jessica Potsou

url = "https://montrealcampus.ca?p="

# Les deux prochaines lignes de commentaires expliquent comment concaténer l'url avec le range de numéros
# for numero in range(20000,30151):
#     print(url+str(numero))

l1 = []

for numero in range(20000,30151):
    l1.append(url+str(numero))

print(l1)
print (len(l1))
