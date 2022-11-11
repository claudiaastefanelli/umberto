#metto 5 alla variabile X, "John" alla variabile Y e lo stampo
x = 5
y = "John"
print(x)
print(y)

print("#############################################")
#attribuisco alla variabile x il valore 4 e il nome "Sally"
x = 4 
print(x)
x = "Sally"
print(x)

print("#################")
#definisco il tipo di variabile 
x = str("claudia")  
y = int(3) 
z = float(3.1)
print(x)
print(y)
print(z)

#assegno alla variabile x il valore intero 5 e alla variabile y John che è una stringa, stampo il tipo variabili con il loro valore
print("##############")
x = 5
y = "John"
print(int(x))
print(str(y))

print("######################")
x = "John"
x = 'John'

print("################")
#nomino la prima variabile a di tipo intero e la seconda A di tipo str
a = 4
A = "Sally"

print("#############")
#attribuire le variabili un nome che non inizi con un numero o non contenga spazi
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print("##############")
#nomino le tre variabili: la prima con le due lettere maiuscole, la seconda con 3 lettere maiuscole, la terza  con il trattino basso
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

print("###########")
#posso assegnare valori a più variabili in una riga:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("#########")
#posso assegnare lo stesso valore a più variabili in una riga:
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("########")
#Se ho una raccolta di valori in un elenco, posso estrarre i valori in variabili (spacchettamento).
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("############")
#print()viene utilizzata per generare variabili.
x = "Python is awesome"
print(x)

print("########")
#in print()funzione, emetti più variabili, separate da una virgola
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print("########")
#metto lo spazio dopo python e is altrimenti stamperebbe la frase attaccata
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print("############")
#Per i numeri, il +carattere funziona come un operatore matematico
x = 5
y = 10
print(x + y)

print("##########")
#in print(), quando provi a combinare una stringa e un numero con l' + operatore, Python ti darà un errore

print("###########")
#per generare più variabili in print() bisogna separarle con virgole, che supportano anche diversi tipi di dati
x = 5
y = "John"
print(x, y)

print ("###########")
#Creo una variabile al di fuori di una funzione e la uso all'interno della funzione
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("##########")
#Creo una variabile all'interno di una funzione, con lo stesso nome della variabile globale
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print("###########")
#Se si utilizza la globalparola chiave, la variabile appartiene all'ambito globale
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("###########")
#Per modificare il valore di una variabile globale all'interno di una funzione, fare riferimento alla variabile usando la globalparola chiave
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("#########")
#le liste vengono create per memorizzare più elementi in una singola variabile
thislist = ["apple", "banana", "cherry"]
print(thislist)

print("############")
#Gli elenchi consentono valori duplicati
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print ("##########")
#Stampa il numero di elementi nell'elenco
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print ("##############")
#Gli elementi dell'elenco possono essere di qualsiasi tipo di dati:stringa, int e booleano
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

print ("###############")
#Un elenco può contenere diversi tipi di dati
list1 = ["abc", 34, True, 40, "male"]
print (list1)

print ("############")
#per stampare il nome della classe a cui appartiene:
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print ("############")
#È anche possibile utilizzare il costruttore list() per creare un elenco:
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print ("##########")
#Stampa solo una voce della lista (es:la seconda "banana")
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print ("#############")
#Indicizzazione negativa significa iniziare dalla fine:-1si riferisce all'ultimo elemento, -2si riferisce al penultimo elemento ecc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print("###########")
#È possibile specicare da dove iniziare e dove terminare l'intervallo ( la ricerca inizierà all'indice 2 (incluso) e terminerà all'indice 5 (non incluso)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print("############")
# il primo elemento ha indice 0
#Questo esempio restituisce gli elementi dall'inizio a, ma NON incluso, "kiwi"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print ("########")
#Questo esempio restituisce gli elementi da "ciliegia" alla fine
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print ("#####")
#Questo esempio restituisce gli elementi da "orange" (-4) a, ma NON include "mango" (-1)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("##########")
#Per determinare se un elemento specifico è presente in un elenco, utilizzare la "in" parola chiave
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print("########")
#Per modificare il valore di un articolo specifico, fare riferimento al numero di indice
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)













