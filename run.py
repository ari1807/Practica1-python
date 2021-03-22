#Quinto desafio
print('Ingrese dos cadenas de texto')
cadena1=input()
cadena2=input()
long_cadena1=len(cadena1)
long_cadena2=len(cadena2)
if (long_cadena1>long_cadena2) :
    print(cadena1)
elif (long_cadena2>long_cadena1):
    print(cadena2)
else:
    print('Ambas cadenas tienen el mismo tamanio')