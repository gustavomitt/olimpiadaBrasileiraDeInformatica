import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)

aves = ["beijaflor","canario","periquito"]
mamiferos = ["anta","sagui","tamandua"]

numeroViveiros = 5;

viveiros = [0 for y in range(numeroViveiros)]

indice=1

respostas=[]

# Ordem sugerida pelo Joel
teste=[]
teste.append({'Mamifero':'anta','Ave':'beijaflor','viveiro':1})
teste.append({'Mamifero':'tamandua','Ave':'periquito','viveiro':2})
teste.append({'Mamifero':'anta','Ave':'beijaflor','viveiro':3})
teste.append({'Mamifero':'sagui','Ave':'beijaflor','viveiro':4})
teste.append({'Mamifero':'anta','Ave':'periquito','viveiro':5})
# Fim da ordem sugerida pelo Joel


for ave1 in aves:
  for mamifero1 in mamiferos:
    viveiros[0] = { 'viveiro': 1,'Ave': ave1, 'Mamifero' : mamifero1 }
    for ave2 in aves:
      for mamifero2 in mamiferos:
        viveiros[1] = { 'viveiro': 2,'Ave': ave2, 'Mamifero' : mamifero2 }
        for ave3 in aves:
          for mamifero3 in mamiferos:
            viveiros[2] = { 'viveiro': 3,'Ave': ave3, 'Mamifero' : mamifero3 }
            for ave4 in aves:
              for mamifero4 in mamiferos:
                viveiros[3] = { 'viveiro': 4,'Ave': ave4, 'Mamifero' : mamifero4 }
                for ave5 in aves:
                  for mamifero5 in mamiferos:
                    viveiros[4] = { 'viveiro': 5,'Ave': ave5, 'Mamifero' : mamifero5 }
                    # verifica a condicao sugerida pelo Joel
                    #if viveiros == teste:
                    #  print "Ordem do Joel encontrada"
                    # fim da verificacao da condicao sugerida pelo Joel
                    condicao1=True
                    for viveiro in viveiros:
                      if viveiro['Ave'] == "canario" and viveiro['Mamifero'] != "anta":
                        condicao1=False
                    condicao2=True
                    for viveiro in viveiros:
                      if viveiro['Mamifero'] == "tamandua" and viveiro['Ave'] == "beijaflor":
                        condicao2=False
                    condicao3=False
                    for viveiro in viveiros:
                      if viveiro['Mamifero'] == "anta" and viveiro['Ave'] == "periquito":
                        condicao3=True
                    condicao4=True
                    for i in range(numeroViveiros):
                      if viveiros[i]['Ave'] == "periquito":
                        if (i>0) and viveiros[i-1]['Ave'] == "periquito":
                          condicao4=False
                        if (i<(numeroViveiros-1)) and viveiros[i+1]['Ave'] == "periquito":
                          condicao4=False
                    condicao5=True
                    for i in range(numeroViveiros):
                      if viveiros[i]['Ave'] == "canario":
                        if (i<(numeroViveiros-1)):
                          for j in range(i,numeroViveiros):
                            if viveiros[j]['Ave'] == "beijaflor":
                              condicao5=False
                    condicao6=False
                    if viveiros[1]['Mamifero'] == "tamandua":
                      condicao6=True
                    if condicao1 and condicao2 and condicao3 and condicao4 and condicao5 and condicao6:
                      print ""
                      print indice,":"
                      indice=indice+1
                      pp.pprint(viveiros)
                      #print viveiros
                      respostas.append(copy.copy(viveiros))


# questao 35
print "Questao 35:"

# opcao A
resultado=True
for resposta in respostas:
  for viveiro in resposta:
    if  viveiro['viveiro'] == 1 and viveiro['Ave'] != "beijaflor":
      resultado=False
      
print "  Opcao A: ",resultado

# opcao B
resultado=True
for resposta in respostas:
  for viveiro in resposta:
    if  viveiro['viveiro'] == 2 and viveiro['Ave'] != "periquito":
      resultado=False
      
print "  Opcao B: ",resultado

# opcao C
resultado=True
for resposta in respostas:
  for viveiro in resposta:
    if  viveiro['viveiro'] == 3 and viveiro['Ave'] != "periquito":
      resultado=False
      
print "  Opcao C: ",resultado

# opcao D
resultado=True
for resposta in respostas:
  for viveiro in resposta:
    if  viveiro['viveiro'] == 4 and viveiro['Mamifero'] != "anta":
      resultado=False
      
print "  Opcao D: ",resultado

# opcao E
resultado=True
for resposta in respostas:
  for viveiro in resposta:
    if  viveiro['viveiro'] == 5 and viveiro['Mamifero'] != "anta":
      resultado=False
      
print "  Opcao E: ",resultado
      
#Questao 36
print "Questao 36:"
# opcao A
resultado=False
for resposta in respostas:
  mamiferos=[]
  for i in range(numeroViveiros):
    mamiferos.append(resposta[i]['Mamifero'])
  if mamiferos == ['anta','tamandua','anta','sagui','tamandua']:
    resultado=True
      
print "  Opcao A: ",resultado

# opcao B
resultado=False
for resposta in respostas:
  mamiferos=[]
  for i in range(numeroViveiros):
    mamiferos.append(resposta[i]['Mamifero'])
  if mamiferos == ['anta','tamandua','sagui','anta','anta']:
    resultado=True
      
print "  Opcao B: ",resultado

# opcao C
resultado=False
for resposta in respostas:
  mamiferos=[]
  for i in range(numeroViveiros):
    mamiferos.append(resposta[i]['Mamifero'])
  if mamiferos == ['anta','tamandua','anta','anta','anta']:
    resultado=True
      
print "  Opcao C: ",resultado
# opcao D
resultado=False
for resposta in respostas:
  mamiferos=[]
  for i in range(numeroViveiros):
    mamiferos.append(resposta[i]['Mamifero'])
  if mamiferos == ['sagui','tamandua','sagui','sagui','anta']:
    resultado=True
      
print "  Opcao D: ",resultado
# opcao E
resultado=False
for resposta in respostas:
  mamiferos=[]
  for i in range(numeroViveiros):
    mamiferos.append(resposta[i]['Mamifero'])
  if mamiferos == ['sagui','tamandua','anta','anta','anta']:
    resultado=True
      
print "  Opcao E: ",resultado


# Funcao consecutivo

def consecutivo( lista, indice, alvo):
  vizinho = [[1],[0,2],[1,3],[2,4],[3]]
  neighbor=False
  for i in vizinho[indice]:
    if lista[i] == alvo:
      neighbor=True
  return neighbor

teste1 = ['sagui','tamandua','anta','anta','anta']
assert consecutivo(teste1,0,'tamandua')
assert not consecutivo(teste1,0,'sagui')
assert consecutivo(teste1,1,'sagui')
assert consecutivo(teste1,1,'anta')
assert not consecutivo(teste1,1,'tamandua')
assert consecutivo(teste1,2,'anta')
assert consecutivo(teste1,2,'tamandua')
assert not consecutivo(teste1,2,'sagui')
assert consecutivo(teste1,3,'anta')
assert not consecutivo(teste1,3,'tamandua')
assert not consecutivo(teste1,3,'sagui')
assert not consecutivo(teste1,4,'tamandua')
assert consecutivo(teste1,4,'anta')







#Questao 37
print "Questao 37:"

#for resposta in respostas:
#  aves=[]
#  mamiferos=[]
#  for i in range(numeroViveiros):
#    aves.append(resposta[i]['Ave'])
#    mamiferos.append(resposta[i]['Mamifero'])
#  if 'beijaflor' in aves and 'canario' in aves:
#    print '  ',aves
#    print '  ', mamiferos
#    print ''
    
# opcao A
resultado=False
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if 'beijaflor' in aves and 'canario' in aves:
    for j in range(numeroViveiros):
      if mamiferos[j] == 'anta':
        if consecutivo(mamiferos,j,'anta'):
          resultado=True

print "  Opcao A: ",resultado

# opcao B
resultado=False
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if 'beijaflor' in aves and 'canario' in aves:
    for j in range(numeroViveiros):
      if aves[j] == 'canario':
        if consecutivo(aves,j,'canario'):
          resultado=True

print "  Opcao B: ",resultado

# opcao C
resultado=False
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if 'beijaflor' in aves and 'canario' in aves:
    for j in range(numeroViveiros):
      if mamiferos[j] == 'sagui':
        resultado=True

print "  Opcao C: ",resultado

# opcao D
resultado=False
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if 'beijaflor' in aves and 'canario' in aves:
    if mamiferos[2] == 'tamandua':
        resultado=True

print "  Opcao D: ",resultado

# opcao E
resultado=False
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if 'beijaflor' in aves and 'canario' in aves:
    if aves.count('periquito') == 2:
        resultado=True

print "  Opcao E: ",resultado

    
#Questao 38
print "Questao 38:"
#for resposta in respostas:
#  aves=[]
#  mamiferos=[]
#  for i in range(numeroViveiros):
#    aves.append(resposta[i]['Ave'])
#    mamiferos.append(resposta[i]['Mamifero'])
#  if aves[4]=='beijaflor':
#    print '  ',aves
#    print '  ',mamiferos
#    print ''

# opcao A
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves[4]=='beijaflor':
    if mamiferos[2] != 'anta':
        resultado=False

print "  Opcao A: ",resultado

# opcao B
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves[4]=='beijaflor':
    if aves.count('beijaflor') != 2:
        resultado=False

print "  Opcao B: ",resultado

# opcao C
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves[4]=='beijaflor':
    if aves.count('canario') != 2:
        resultado=False

print "  Opcao C: ",resultado

# opcao D
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves[4]=='beijaflor':
    for j in range(numeroViveiros):
      if mamiferos[j] == 'sagui':
        if consecutivo(mamiferos,j,'sagui'):
          resultado=False

print "  Opcao D: ",resultado

# opcao E
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves[4]=='beijaflor':
    for j in range(numeroViveiros):
      if 'sagui' in mamiferos:
        if mamiferos[3] != 'sagui':
          resultado=False

print "  Opcao E: ",resultado


#Questao 39
print "Questao 39:"
#for resposta in respostas:
#  aves=[]
#  mamiferos=[]
#  for i in range(numeroViveiros):
#    aves.append(resposta[i]['Ave'])
#    mamiferos.append(resposta[i]['Mamifero'])
#  if aves.count('beijaflor')==2:
#    print '  ',aves
#    print '  ',mamiferos
#    print ''

# opcao A
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves.count('beijaflor') == 2:
    if mamiferos[3] != 'anta':
        resultado=False

print "  Opcao A: ",resultado

# opcao B
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves.count('beijaflor') == 2:
    if mamiferos[4] != 'anta':
        resultado=False

print "  Opcao B: ",resultado

# opcao C
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves.count('beijaflor') == 2:
    for j in range(numeroViveiros):
      if aves[j] == 'beijaflor':
        if not consecutivo(aves,j,'canario'):
          resultado=False

print "  Opcao C: ",resultado

# opcao D
antas=0
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves.count('beijaflor') == 2:
    for j in range(numeroViveiros):
      if aves[j] == 'beijaflor':
        if mamiferos.count('anta') > antas:
          antas=mamiferos.count('anta')
resultado = (antas == 4)

print "  Opcao D: ",resultado

# opcao E
resultado=True
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves.count('beijaflor') == 2:
    for j in range(numeroViveiros):
      if mamiferos[j] == 'sagui':
        if consecutivo(mamiferos,j,'sagui'):
          resultado=False

print "  Opcao E: ",resultado


#Questao 40
print "Questao 40:"
#for resposta in respostas:
#  aves=[]
#  mamiferos=[]
#  for i in range(numeroViveiros):
#    aves.append(resposta[i]['Ave'])
#    mamiferos.append(resposta[i]['Mamifero'])
#  if aves.count('canario')==2:
#    print '  ',aves
#    print '  ',mamiferos
#    print ''

doisCanarios = []
for resposta in respostas:
  aves=[]
  mamiferos=[]
  for i in range(numeroViveiros):
    aves.append(resposta[i]['Ave'])
    mamiferos.append(resposta[i]['Mamifero'])
  if aves.count('canario')==2:
    doisCanarios.append(copy.copy(resposta))

avesIguais=[1,1,1,1,1]
mamiferosIguais=[1,1,1,1,1]
for result in doisCanarios:
  for i in range(numeroViveiros):
    if result[i]['Ave'] != doisCanarios[0][i]['Ave']:
      avesIguais[i] = 0 
    if result[i]['Mamifero'] != doisCanarios[0][i]['Mamifero']:
      mamiferosIguais[i] = 0 
resultado = sum(avesIguais)+sum(mamiferosIguais)

print "  Tipos determinados: ",resultado

