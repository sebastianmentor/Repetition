person2 = {'namn':'Kalle', 'ålder':12, 'stad':'Köping', 'familj':[]}
person3 = {'namn':'Sanna', 'ålder':20, 'stad':'Stockholm', 'familj':[]}
person1 = {'namn':'Sebastian', 'ålder':42, 'stad':'Västerås', 'familj':[person2, person3]}
person4 = {'namn':'Elin', 'ålder':50, 'stad':'Arboga', 'familj':[]}

lista_med_personer = [person4,person1,person2,person3]

def mini_program():
    print('kör något underprogram för att underlätta för oss!!')


def extrahera_en_persons_namn(person):
    return person['namn']



for person in lista_med_personer:
    print(extrahera_en_persons_namn(person))