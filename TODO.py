#Fechas
import datetime
from datetime import datetime,date,timedelta,time

#Notificaciones
from win10toast import ToastNotifier

#Título de la notificación
header_text = []
#Cuerpo de la notificación
text_todo = []
#Fechas de asignación de deberes
dead_line = []
#Una semana antes
one_week_notify = []
#Cinco días antes
five_days_notify = []
#Tres días antes
three_day_notify = []


#Guardar datos con formato de fecha
def cast_month(month):
    months = [
        "Nothing","Ene","Feb","Marzo","Abril",
        "Mayo","Junio","Julio",
        "Ago","Sep","Oct","Nov","Dic"
    ]

    return months.index(month)

#Pedir datos
def data_form():
    #Fechas
    day = int(input("Día> "))
    month = input("Mes>")
    year = int(input("Año> "))

    #La asignatura será utilizada como título de la notificación
    header_text.append(input("Clase> "))
    
    #La actividad o tarea será el cuerpo de la notificación
    text_todo.append(input("TODO> "))
    
    #Formato de la fecha 
    dead_line.append(date(year,cast_month(month),day))
    print(type(date(year,cast_month(month),day)))

#Avisar una semana antes la tarea a realizar
def notify_me():
    #Por cada día en el arreglo de fecha
    for day in dead_line:
        
        #Verifica si coincide la fecha de hoy con alguna del arreglo
        if(date.today() == day or date.today()):
        
            #Si coincide entonces dame en índice de la fecha
            reference = dead_line.index(day)
        
            #Lanza una notificación
            notification = ToastNotifier()
            notification.show_toast(
        
                #Usando la referencia del indice, puedo buscar 
                #los elementos que tengo que mostrar de los 
                #otros arreglos
                header_text[reference],
                text_todo[reference],
                duration = 10
            )

            #Elimo el elemento de la lista
            dead_line.pop(day)
            print(dead_line)



if __name__ == "__main__":
    option = "y"
    while option == "y":
        data_form()
        option = input("Again? [y/n]> ")

    notify_me()
    
