variabel = None

min_lista = [1,2,'str', variabel] # osv osv
# print(type(min_lista))
min_lista.append(3.4)
min_lista.extend(['Texter', 8888, 2j])
min_lista.remove('str')

print(min_lista)

ny_lista = [1,2,3,4]

print(min_lista + ny_lista)