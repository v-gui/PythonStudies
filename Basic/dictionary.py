# dictionary = Modificavel, coleção sem ordem de valores unicos: keys:valores.
# rapido, porque utiliza hashing, permitindo o acesso rapido dos valores.

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China': 'Beijing',
            'Russia':'Moscow'}


capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Florida'})
capitals.pop('China')  #Excluir
capitals.clear() #Limpar tudo

#print(capitals['Germany'])
#print(capitals.get('Germany'))  # método mais seguro
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())


for key,value in capitals.items():
    print(key, value)