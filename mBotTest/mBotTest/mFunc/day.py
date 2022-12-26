from datetime import date

num = date.today().weekday()

def getDay():
    sem = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado-feira", "Domingo-feira")
    return sem[num]


print(getDay())