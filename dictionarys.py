# var1 = 'värde1'
# var2 = 'värde2'
# var3 = 'värde3'
# var4 = 'värde4'
# var5 = 'värde5'
# var6 = 'värde6'
# var7 = 'värde7'
# var8 = 'värde8'
# var9 = 'värde9'
# var10 = 'värde10'
# var11 = 'värde11'
# var12 = 'värde12'

# dictionary_med_mina_värden = {}

var = {}

var[1] = 'värde1'
var[2] = 'värde2'
var[3] = 'värde3' 
var[4] = 'värde4'
var[5] = 'värde5'
var[6] = 'värde6'
var[7] = 'värde7'
var[8] = 'värde8'
var[9] = 'värde9'
var[10] = 'värde10'
var[11] = 'värde11'
var[12] = 'värde12'


# print(var[12])

person2 = {'namn':'Kalle', 'ålder':12, 'stad':'Köping', 'familj':[]}
person3 = {'namn':'Sanna', 'ålder':20, 'stad':'Stockholm', 'familj':[]}
person1 = {'namn':'Sebastian', 'ålder':42, 'stad':'Västerås', 'familj':[person2, person3]}

lista_med_personer = [person1,person2,person3]

# print(person1['stad'])

extrahera_namn = []
extrahera_familj = {}

for person in lista_med_personer:
    extrahera_namn.append(person['namn'])

    familjen = person['familj']

    if not familjen == []:
            extrahera_familj[person['namn']] = familjen


    # print(person['namn'])

print(f"Jag extraherade den datan jag ville och fick följande {extrahera_namn}")
print(f"Jag extraherade den datan jag ville och fick följande {extrahera_familj}")