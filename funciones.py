from datetime import date, datetime
import os
from os import system

fecha_Completa = str(date.today())
dt = datetime.now()
fecha_Año = str(dt.year)
fecha_Mes = str(dt.month)
fecha_Dia = str(dt.day)
ruta_Año = "/opt/home/cristian.gil/Prueba/" + fecha_Año
ruta_Mes = "/opt/home/cristian.gil/Prueba/" + fecha_Año + "/" + fecha_Mes
ruta_Dia = "/opt/home/cristian.gil/Prueba/" + fecha_Año + "/" + fecha_Mes + "/" + fecha_Dia

def validar_Ruta_Año (ruta_Año):
    if os.path.isdir(ruta_Año):
        #return "EL DIRECTORIO " + ruta_Año + " Existe"
        print("El directorio: " + ruta_Año + " existe")
        if os.path.isdir(ruta_Mes):
            #return "EL DIRECTORIO " + ruta_Año + " Existe"
            print("El directorio: " + ruta_Mes + " existe")
            if os.path.isdir(ruta_Dia):
                #return "EL DIRECTORIO " + ruta_Año + " Existe"
                print("El directorio: " + ruta_Dia + " existe")
            else:
                print ("El directorio: " + ruta_Dia + " no existe")
                try:
                    os.mkdir(ruta_Dia)
                except OSError:
                    print("La creación del directorio %s falló" % ruta_Dia)
                else:
                    print("Se ha creado el directorio: %s " % ruta_Dia)

        else:
            print ("El directorio: " + ruta_Mes + " no existe")
            try:
                os.mkdir(ruta_Mes)
                if os.path.isdir(ruta_Dia):
                    #return "EL DIRECTORIO " + ruta_Año + " Existe"
                    print("El directorio: " + ruta_Dia + " existe")
                else:
                    print ("El directorio: " + ruta_Dia + " no existe")
                    try:
                        os.mkdir(ruta_Dia)
                    except OSError:
                        print("La creación del directorio %s falló" % ruta_Dia)
                    else:
                        print("Se ha creado el directorio: %s " % ruta_Dia)
            except OSError:
                print("La creación del directorio %s falló" % ruta_Mes)
            else:
                print("Se ha creado el directorio: %s " % ruta_Mes)
    else:
        print ("El directorio: " + ruta_Año + " no existe")
        try:
            os.mkdir(ruta_Año)
            if os.path.isdir(ruta_Mes):
                #return "EL DIRECTORIO " + ruta_Año + " Existe"
                print("El directorio: " + ruta_Mes + " existe")
            else:
                print ("El directorio: " + ruta_Mes + " no existe")
                try:
                    os.mkdir(ruta_Mes)
                    if os.path.isdir(ruta_Dia):
                        #return "EL DIRECTORIO " + ruta_Año + " Existe"
                        print("El directorio: " + ruta_Dia + " existe")
                    else:
                        print ("El directorio: " + ruta_Dia + " no existe")
                        try:
                            os.mkdir(ruta_Dia)
                        except OSError:
                            print("La creación del directorio %s falló" % ruta_Dia)
                        else:
                            print("Se ha creado el directorio: %s " % ruta_Dia)

                except OSError:
                    print("La creación del directorio %s falló" % ruta_Mes)
                else:
                    print("Se ha creado el directorio: %s " % ruta_Mes)

        except OSError:
            print("La creación del directorio %s falló" % ruta_Año)
        else:
            print("Se ha creado el directorio: %s " % ruta_Año)
print(validar_Ruta_Año(ruta_Año))