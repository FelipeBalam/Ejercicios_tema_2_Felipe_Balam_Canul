import re 

txt  = """ ideapad Mferrol disco duro mytec sms clave de "mensaje" en "celulares" los ipes son 
10.255.255.255, 172.16.0.0, 172.31.255.255, 192.168.0.0, 192.168.255.255
la hora es 03:00 pm, 04:00 pm, 05:00 pm, 07:00 pm, 05:30 pm, 04:55 pm, 12:00 pm entre otros 
correo electrónico : felipe.balamcanul@gmail.com, eduardo173@gmail.com, canchefrancisca@gmail.com
Ejemplos de URLs: www.google.com, www.amazon.com, www.facebook.com
Códigos postales :77121, 97780, 34679, 98765 """

print(" 1.	Todas las palabras que tengan una longitud de 7 o más letras ")
funcion= r"[A-Za-záéíóú]{7,}"

palabras = re.findall(funcion,txt)

for acumpalabras in palabras:
    print(acumpalabras)    

print(" 2.	Expresiones que NO finalicen con una vocal. ")
x = r"[A-Za-záéíóú]{1,}[^aeiou\s\W]\b"

xpalabras = re.findall(x,txt)

for xacumulador in xpalabras:
    print(xacumulador)

print(" 3.	Las palabras que inicien con “M” donde la segunda letra no sea vocal ")
y = r"[M][^aeiouáéíóú]\w{1,}"

ypalabras = re.findall(y,txt)

for yacumulador in ypalabras:
    print(yacumulador)

print(" 4.	Expresiones encerradas entre comillas ")
u= r"(\"[\w\s]+\")"

upalabras = re.findall(u,txt)

for uacumulador in upalabras:
    print(uacumulador)

print(" 5.	Ip’s ")
v= r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

vpalabras = re.findall(v,txt)

for vacumulador in vpalabras:
    print(vacumulador)

print(" 6.	Horas ")
g= r"[0-9]{1,2}\:[0-9]{1,2}\s[a/p][m]"

gpalabras = re.findall(g,txt)

for gacumulador in gpalabras:
    print(gacumulador)

print(" 7.	Telefonos ")

texto = ''' Mi teléfono es 600678899
Mi nuevo número es el 678.000.102
Si llamas desde fuera de españa +34.708.56.78.98 '''
 
listadoTelfs = list(map(lambda posibTelf: re.sub(r'\D', '', posibTelf), re.findall(r'\b[\d\.]+\b', texto)))
listadoTelfs = list(filter(bool, listadoTelfs))
 
print(listadoTelfs)

print(" 8.	Correos electrónicos ")
e= r"\w+[\@]+\w+[.]+\w+"

epalabras = re.findall(e,txt)

for eacumulador in epalabras:
    print(eacumulador)

print(" 9.	Url’s ")
j= r"[Ww]+\w[.]\w+[.]\w+"

jpalabras = re.findall(j,txt)

for jacumulador in jpalabras:
    print(jacumulador)

print(" 10.	Código postal ")
I= r"[0-9]{5}"

Ipalabras = re.findall(I,txt)

for Iacumulador in Ipalabras:
    print(Iacumulador)