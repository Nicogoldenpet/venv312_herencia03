#Fecha: 06/06/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

#Importando los módulos y las librerias
import msvcrt
import platform
import os
from colorama import Fore,init, just_fix_windows_console
import Modules.clases as clases


def ingreso(): #Definiendo la función de ingreso
    print(Fore.LIGHTBLUE_EX)
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                            BIENVENIDO AL PROGRAMA DE HERENCIAS #3                                                                                                       |")
    print("|                                                                                            PARA INGRESAR PRESIONE CUALQUIER TECLA                                                                                                       |")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                                                                                                                                                                         |")
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    msvcrt.getch()
    limpiar_pantalla()
    

def limpiar_pantalla(): #Definiendo la función para limpiar pantalla
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def leer_datos(): #Definiendo la función para leer todos los datos de las siete clases
    print(Fore.LIGHTYELLOW_EX, "Iniciaremos registrando un docente a tiempo completo.")
    print(Fore.LIGHTBLUE_EX)
    docen1 = clases.TiempoCompleto("","","","","","","","","","") #Instanciando el docente 1 para la clase TiempoCompleto
    docen1.leer_id_estrato(10,10) #Leyendo el documento
    docen1.leer_nombre() #Leyendo el nombre
    docen1.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    docen1.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    docen1.set__genero(input("Ingrese su género: ")) #Leyendo el género
    docen1.leer_id_estrato(1,2) #Leyendo el estrato
    docen1.leer_docente() #Leyendo los datos del docente
    docen1.set__categoria(input("Ingrese su categoría: ")) #Leyendo la categoría
    docen1.leer_puntos_salario(1,3) #Leyendo los puntos
    docen1.leer_puntos_salario(5,8) #Leyendo el salario

    docen1.informacion()
    docen1.sueldo()
    docen1.liquidarTC()
    docen1.mostrar_dg()
    docen1.calcular_eps()
    docen1.calcular_pension()
    docen1.calcular_arl()
    docen1.calcular_sena()
    docen1.calcular_cajas()
    docen1.calcular_icbf()
    docen1.calcular_auxilio()

    print(Fore.LIGHTYELLOW_EX, "Pulse cualquier tecla para continuar")
    msvcrt.getwch()
    limpiar_pantalla()

    print("Seguiremos registrando un docente ocasional.")
    print(Fore.LIGHTBLUE_EX)
    docen2 = clases.Ocasionales("","","","","","","","","","") #Instanciando el docente 2 para la clase Ocasionales
    docen2.leer_id_estrato(10,10) #Leyendo el documento
    docen2.leer_nombre() #Leyendo el nombre
    docen2.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    docen2.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    docen2.set__genero(input("Ingrese su género: ")) #Leyendo el género
    docen2.leer_id_estrato(1,2) #Leyendo el estrato
    docen2.leer_docente() #Leyendo los datos del docente
    docen2.set__ultimotitulo(input("Ingrese su último título: ")) #Leyendo el último título profesional
    docen2.leer_numeses_salario(1,3) #Leyendo los meses que trabaja
    docen2.leer_numeses_salario(5,8) #Leyendo el salario

    docen2.informacion()
    docen2.sueldo()
    docen2.liquidarTC()
    docen2.mostrar_dg()
    docen2.calcular_eps()
    docen2.calcular_pension()
    docen2.calcular_arl()
    docen2.calcular_sena()
    docen2.calcular_cajas()
    docen2.calcular_icbf()
    docen2.calcular_auxilio()

    print(Fore.LIGHTYELLOW_EX, "Pulse cualquier tecla para continuar")
    msvcrt.getwch()
    limpiar_pantalla()

    print("A continuación registraremos un docente en hora cátedra.")
    print(Fore.LIGHTBLUE_EX)
    docen3 = clases.HoraCatedra("","","","","","","","","","") #Instanciando el docente 3 para la clase HoraCatedra
    docen3.leer_id_estrato(10,10) #Leyendo el documento
    docen3.leer_nombre() #Leyendo el nombre
    docen3.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    docen3.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    docen3.set__genero(input("Ingrese su género: ")) #Leyendo el género
    docen3.leer_id_estrato(1,2) #Leyendo el estrato
    docen3.leer_docente() #Leyendo los datos del docente
    docen3.set__ultimotitulo(input("Ingrese su último título: ")) #Leyendo el último título profesional
    docen3.leer_numhoras_contrato_salario(1,3) #Leyendo las horas que trabaja
    docen3.leer_numhoras_contrato_salario(5,10) #Leyendo el valor del contrato
    docen3.leer_numhoras_contrato_salario(5,8) #Leyendo el salario

    docen3.informacion()
    docen3.sueldo()
    docen3.liquidarTC()
    docen3.mostrar_dg()
    docen3.calcular_eps()
    docen3.calcular_pension()
    docen3.calcular_arl()
    docen3.calcular_sena()
    docen3.calcular_cajas()
    docen3.calcular_icbf()
    docen3.calcular_auxilio()

    print(Fore.LIGHTYELLOW_EX, "Pulse cualquier tecla para continuar")
    msvcrt.getwch()
    limpiar_pantalla()

    print("Terminando con los docentes, ahora registraremos a un administrativo OPS")
    print(Fore.LIGHTBLUE_EX)
    admin1 = clases.Ops("","","","","","","","","") #Instanciando admin 1 para la clase OPS
    admin1.leer_id_estrato(10,10) #Leyendo el documento
    admin1.leer_nombre() #Leyendo el nombre
    admin1.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    admin1.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    admin1.set__genero(input("Ingrese su género: ")) #Leyendo el género
    admin1.leer_id_estrato(1,2) #Leyendo el estrato
    admin1.leer_administrativos() #Leyendo los datos del administrador
    admin1.set__fechavinculacion(input("Ingrese su fecha de vinculación (En formato dd-mm-yy): ")) #Leyendo la fecha de vinculación
    admin1.leer_numeses_contrato_salario(1,3) #Leyendo los meses que trabaja
    admin1.leer_numeses_contrato_salario(5,10) #Leyendo el valor del contrato
    admin1.leer_numeses_contrato_salario(5,8) #Leyendo el salario

    admin1.informacion()
    admin1.liquidarOPS()
    admin1.mostrar_dg()
    admin1.calcular_eps()
    admin1.calcular_pension()
    admin1.calcular_arl()
    admin1.calcular_sena()
    admin1.calcular_cajas()
    admin1.calcular_icbf()
    admin1.calcular_auxilio()

    print(Fore.LIGHTYELLOW_EX, "Pulse cualquier tecla para continuar")
    msvcrt.getwch()
    limpiar_pantalla()

    print("A continuación registraremos a un administrativo de planta auxiliar")
    print(Fore.LIGHTBLUE_EX)
    admin2 = clases.Auxiliar("","","","","","","","","") #Instanciando admin 2 para la clase Auxiliar
    admin2.leer_id_estrato(10,10) #Leyendo el documento
    admin2.leer_nombre() #Leyendo el nombre
    admin2.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    admin2.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    admin2.set__genero(input("Ingrese su género: ")) #Leyendo el género
    admin2.leer_id_estrato(1,2) #Leyendo el estrato
    admin2.leer_administrativos() #Leyendo los datos del administrador
    admin2.set__fechavinculacion(input("Ingrese su fecha de vinculación (En formato dd-mm-yy): ")) #Leyendo la fecha de vinculación
    admin2.leer_nivel_salario(1,2) #Leyendo el nivel
    admin2.leer_nivel_salario(5,8) #Leyendo el salario

    admin2.informacion()
    admin2.sueldo()
    admin2.liquidarAux()
    admin2.mostrar_dg()
    admin2.calcular_eps()
    admin2.calcular_pension()
    admin2.calcular_arl()
    admin2.calcular_sena()
    admin2.calcular_cajas()
    admin2.calcular_icbf()
    admin2.calcular_auxilio()

    print(Fore.LIGHTYELLOW_EX, "Pulse cualquier tecla para continuar")
    msvcrt.getwch()
    limpiar_pantalla()

    print("Seguido de esto registraremos un administrador de planta técnico")
    print(Fore.LIGHTBLUE_EX)
    admin3 = clases.Tecnico("","","","","","","","","") #Instanciando admin 3 para la clase Técnico
    admin3.leer_id_estrato(10,10) #Leyendo el documento
    admin3.leer_nombre() #Leyendo el nombre
    admin3.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    admin3.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    admin3.set__genero(input("Ingrese su género: ")) #Leyendo el género
    admin3.leer_id_estrato(1,2) #Leyendo el estrato
    admin3.leer_administrativos() #Leyendo los datos del administrador
    admin3.set__fechavinculacion(input("Ingrese su fecha de vinculación (En formato dd-mm-yy): ")) #Leyendo la fecha de vinculación
    admin3.leer_nivel_salario(1,2) #Leyendo el nivel
    admin3.leer_nivel_salario(5,8) #Leyendo el salario

    admin3.informacion()
    admin3.sueldo()
    admin3.liquidarTec()
    admin3.mostrar_dg()
    admin3.calcular_eps()
    admin3.calcular_pension()
    admin3.calcular_arl()
    admin3.calcular_sena()
    admin3.calcular_cajas()
    admin3.calcular_icbf()
    admin3.calcular_auxilio()

    print(Fore.LIGHTYELLOW_EX, "Pulse cualquier tecla para continuar")
    msvcrt.getwch()
    limpiar_pantalla()

    print("Por último registraremos un administrador de planta profesional")
    print(Fore.LIGHTBLUE_EX)
    admin4 = clases.Profesional("","","","","","","","","") #Instanciando admin 4 para la clase Profesional
    admin4.leer_id_estrato(10,10) #Leyendo el documento
    admin4.leer_nombre() #Leyendo el nombre
    admin4.set__fechanacimiento(input("Ingrese su fecha de nacimiento: ")) #Leyendo la fecha de nacimiento
    admin4.set__ciudadnacimiento(input("Ingrese la ciudad en la que nació: ")) #Leyendo la ciudad de nacimiento
    admin4.set__genero(input("Ingrese su género: ")) #Leyendo el género
    admin4.leer_id_estrato(1,2) #Leyendo el estrato
    admin4.leer_administrativos() #Leyendo los datos del administrador
    admin4.set__fechavinculacion(input("Ingrese su fecha de vinculación (En formato dd-mm-yy): ")) #Leyendo la fecha de vinculación
    admin4.leer_nivel_salario(1,2) #Leyendo el nivel
    admin4.leer_nivel_salario(5,8) #Leyendo el salario

    admin4.informacion()
    admin4.sueldo()
    admin4.liquidarProf()
    admin4.mostrar_dg()
    admin4.calcular_eps()
    admin4.calcular_pension()
    admin4.calcular_arl()
    admin4.calcular_sena()
    admin4.calcular_cajas()
    admin4.calcular_icbf()
    admin4.calcular_auxilio()