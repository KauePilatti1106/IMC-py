"""Solicite para o usuario informar:
    - Nome
    - Altura (cm)
    - Peso (kg)
    Com base nestes dados realize o calculo para 
    descobrir qual o IMC (indice de massa corporea)
    da pessoa.
    Para o calculo utilize a tabela padrão do IMC.
    abaixo de 18,5 - Abaixo do Peso (Pegue suplementos do Cariani)
    entre 18,6 e 24,9 - Peso Ideal (Para Bens)
    entre 25,0 e 29,9 - Sobrepeso
    entre 30,0 e 34,9 - Obesidade Grau 1
    entre 35,0 e 39,9 - Obesidade Grau 2
    acima de 40,0 - Obesidade Grau 3 (Dr. Nowzaradan te espera)
    formula: IMC = peso / altura²"""

nome= input ("Qual o nome?")
altura= int(input ("Qual a altura em cemtimetros?"))
peso= float(input("Qual o pesso?"))

Formula_IMC= peso/(altura**2)

texto=f'''
O nome do usuario é: {nome}
A altura do usuario é: {altura}
O peso do usuario é: {peso}
A massa do usurio é: {Formula_IMC}
Eesse usuario está:'''

print(texto)

if Formula_IMC >=18.5:
    print ("Abaixo do peso(Pegue suplemento de Cariami)")
elif Formula_IMC <=18.6 and Formula_IMC >= 24.9:
    print ("Peso ideal(Parabens)")
elif Formula_IMC <=25.0 and Formula_IMC>=29.9:
    print ("Sobrepeso")
elif Formula_IMC <=30.0 and Formula_IMC >=34.9:
    print ("Obsidade Grau 1")
elif Formula_IMC <= 35.0 and Formula_IMC >=39.9:
   print ("Obesidade Grau 2")
elif Formula_IMC <= 40.0:
     print ("Obesidade Grau 3 (Dr. Nowzaran tre espera)")



