#Fecha: 06/06/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

from datetime import datetime, timedelta

class Persona: #Definiendo la clase padre
    def __init__(self,idpersona=0, nombre='', apellido='', fechanacimiento='', ciudadnacimiento='', genero='', estrato=0): #Método constructor
        self.__idpersona=idpersona
        self.__nombre=nombre
        self.__apellido=apellido
        self.__fechanacimiento=fechanacimiento
        self.__ciudadnacimiento=ciudadnacimiento
        self.__genero=genero
        self.__estrato=estrato

    #Métodos getter y setter para los valores
    def get__idpersona(self):
        return self.__idpersona
    

    def set__idpersona(self, value):
        self.__idpersona = value
    

    def get__nombre(self):
        return self.__nombre
    

    def set__nombre(self, value):
        self.__nombre=value


    def get__apellido(self):
        return self.__apellido
    

    def set__apellido(self, value):
        self.__apellido=value


    def get__fechanacimiento(self):
        return self.__fechanacimiento
    

    def set__fechanacimiento(self, value):
        self.__fechanacimiento = value
    

    def get__ciudadnacimiento(self):
        return self.__ciudadnacimiento
    

    def set__ciudadnacimiento(self, value):
        self.__ciudadnacimiento=value


    def get__genero(self):
        return self.__genero
    

    def set__genero(self, value):
        self.__genero=value


    def get__estrato(self):
        return self.__estrato
    

    def set__estrato(self, value):
        self.__estrato=value
        

    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 13, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Código aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Código aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.") 


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}.'.format(self.get__idpersona(), self.get__nombre(), self.get__apellido(), 
                                                                                                                            self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato()))
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")


class Docente(Persona): 
    def __init__(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion='', tituloprofesion='', unidadacademica=''): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato)
        self.__areaformacion=areaformacion
        self.__tituloprofesion=tituloprofesion
        self.__unidadacademica=unidadacademica


    #Métodos getter y setter para los siguientes valores
    def get__areaformacion(self):
        return self.__areaformacion
    

    def set__areaformacion(self, value):
        self.__areaformacion = value


    def get__tituloprofesion(self):
        return self.__tituloprofesion
    

    def set__tituloprofesion(self, value):
        self.__tituloprofesion = value


    def get__unidadacademica(self):
        return self.__unidadacademica
    

    def set__unidadacademica(self, value):
        self.__unidadacademica = value


    def solo_num(value): #Creando una función para leer números
        while True:
            if (value.isnumeric()):
                return True
            else:
                return False
            

    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_docente(self): #Definiendo la función para leer los datos del docente
        while True:
            area =  str(input("Ingrese su área de formación: "))
            if (area.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el área
                self.set__areaformacion(area)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        while True: #Ahora pasará a aprobar la unidad académica
                            unidad =  str(input("Ingrese su única académica: "))
                            if (unidad.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la unidad
                                self.set__unidadacademica(unidad)
                                break #Cerrando el ciclo
                            else: #Si el usuario ingresa números no las acepta.
                                print("Solo se permiten caracteres alfabéticos y espacios.")
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi área de formación es {7}, tengo un título profesional en {8} y mi unidad académica es {9}'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__areaformacion(), self.get__tituloprofesion(),
               self.get__unidadacademica()))
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")


class TiempoCompleto(Docente):

    def __init__(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion, tituloprofesion, unidadacademica, categoria='', puntos=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion, tituloprofesion, unidadacademica)
        self.__categoria=categoria
        self.__puntos=puntos
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__categoria(self):
        return self.__categoria
    

    def set__categoria(self, value):
        self.__categoria = value


    def get__puntos(self):
        return self.__puntos
    

    def set__puntos(self, value):
        self.__puntos = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_docente(self): #Definiendo la función para leer los datos del docente
        while True:
            area =  str(input("Ingrese su área de formación: "))
            if (area.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el área
                self.set__areaformacion(area)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        while True: #Ahora pasará a aprobar la unidad académica
                            unidad =  str(input("Ingrese su única académica: "))
                            if (unidad.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la unidad
                                self.set__unidadacademica(unidad)
                                break #Cerrando el ciclo
                            else: #Si el usuario ingresa números no las acepta.
                                print("Solo se permiten caracteres alfabéticos y espacios.")
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_puntos_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 3: #Unicamente si el valor ingresado es 3, se registrará como puntos
                value = str(input("Ingrese la cantidad de puntos que realizó: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un dato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 3, no lo acepta
                            print("No puede colocar un dato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__puntos(value) #Puntos aprobados
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi área de formación es {7}, tengo un título profesional en {8} y mi unidad académica es {9}. Soy de categoría {10} y realicé {11} puntos'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__areaformacion(), self.get__tituloprofesion(),
               self.get__unidadacademica(), self.get__categoria(), self.get__puntos()))
        
        
    def sueldo(self): #Mostrando el sueldo del docente
        print("Mi sueldo es de {0}".format(self.get__salario()))
        
        
    def liquidarTC(self): #Mostrando la liquidación TC
        print("Calculando la liquidación TC...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")
        

class Ocasionales(Docente):

    def __init__(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion, tituloprofesion, unidadacademica, ultimotitulo='', numeses=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion, tituloprofesion, unidadacademica)
        self.__ultimotitulo=ultimotitulo
        self.__numeses=numeses
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__ultimotitulo(self):
        return self.__ultimotitulo
    

    def set__ultimotitulo(self, value):
        self.__ultimotitulo = value


    def get__numeses(self):
        return self.__numeses
    

    def set__numeses(self, value):
        self.__numeses = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_docente(self): #Definiendo la función para leer los datos del docente
        while True:
            area =  str(input("Ingrese su área de formación: "))
            if (area.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el área
                self.set__areaformacion(area)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        while True: #Ahora pasará a aprobar la unidad académica
                            unidad =  str(input("Ingrese su única académica: "))
                            if (unidad.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la unidad
                                self.set__unidadacademica(unidad)
                                break #Cerrando el ciclo
                            else: #Si el usuario ingresa números no las acepta.
                                print("Solo se permiten caracteres alfabéticos y espacios.")
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_numeses_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 3: #Unicamente si el valor ingresado es 3, se registrará como meses
                value = str(input("Ingrese el número de meses que trabaja: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un dato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 3, no lo acepta
                            print("No puede colocar un dato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__numeses(value) #Dato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi área de formación es {7}, tengo un título profesional en {8} y mi unidad académica es {9}. Mi último título es {10} y trabajo desde hace {11} meses'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__areaformacion(), self.get__tituloprofesion(),
               self.get__unidadacademica(), self.get__ultimotitulo(), self.get__numeses()))
        
        
    def sueldo(self): #Mostrando el sueldo del docente
        print("Mi sueldo es de {0}".format(self.get__salario()))
        
        
    def liquidarTC(self): #Mostrando la liquidación TC
        print("Calculando la liquidación TC...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")
        

class HoraCatedra(Docente):

    def __init__(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion, tituloprofesion, unidadacademica, ultimotitulo='', numhoras=0, valorcontrato=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, areaformacion, tituloprofesion, unidadacademica)
        self.__ultimotitulo=ultimotitulo
        self.__numhoras=numhoras
        self.__valorcontrato=valorcontrato
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__ultimotitulo(self):
        return self.__ultimotitulo
    

    def set__ultimotitulo(self, value):
        self.__ultimotitulo = value


    def get__numhoras(self):
        return self.__numhoras
    

    def set__numhoras(self, value):
        self.__numhoras = value


    def get__valorcontrato(self):
        return self.__valorcontrato
    

    def set__valorcontrato(self, value):
        self.__valorcontrato = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_docente(self): #Definiendo la función para leer los datos del docente
        while True:
            area =  str(input("Ingrese su área de formación: "))
            if (area.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el área
                self.set__areaformacion(area)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        while True: #Ahora pasará a aprobar la unidad académica
                            unidad =  str(input("Ingrese su única académica: "))
                            if (unidad.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la unidad
                                self.set__unidadacademica(unidad)
                                break #Cerrando el ciclo
                            else: #Si el usuario ingresa números no las acepta.
                                print("Solo se permiten caracteres alfabéticos y espacios.")
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_numhoras_contrato_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 3: #Unicamente si el valor ingresado es 3, se registrará como horas
                value = str(input("Ingrese el número de horas que trabaja a la semana: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un dato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 3, no lo acepta
                            print("No puede colocar un dato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__numhoras(value) #Dato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 10: #Unicamente si el valor ingresado es 10, se registrará como valor de contrato
                value = str(input("Ingrese su valor de contrato: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__valorcontrato(value) #Valor aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Docente.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi área de formación es {7}, tengo un título profesional en {8} y mi unidad académica es {9}. Mi último título es {10}, trabajo {11} horas a la semana y mi valor de contrato es {12}'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__areaformacion(), self.get__tituloprofesion(),
               self.get__unidadacademica(), self.get__ultimotitulo(), self.get__numhoras(), self.get__valorcontrato()))
        
        
    def sueldo(self): #Mostrando el sueldo del docente
        print("Mi sueldo es de {0}".format(self.get__salario()))
        
        
    def liquidarTC(self): #Mostrando la liquidación TC
        print("Calculando la liquidación TC...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")
        

class Administrativos(Persona): 
    def __init__(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia='', tituloprofesion=''): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato)
        self.__dependencia=dependencia
        self.__tituloprofesion=tituloprofesion


    #Métodos getter y setter para los siguientes valores
    def get__dependencia(self):
        return self.__dependencia
    

    def set__dependencia(self, value):
        self.__dependencia = value


    def get__tituloprofesion(self):
        return self.__tituloprofesion
    

    def set__tituloprofesion(self, value):
        self.__tituloprofesion = value


    def solo_num(value): #Creando una función para leer números
        while True:
            if (value.isnumeric()):
                return True
            else:
                return False
            

    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_administrativos(self): #Definiendo la función para leer los datos del administrador
        while True:
            dependencia =  str(input("Ingrese su lugar de dependencia: "))
            if (dependencia.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la dependencia
                self.set__dependencia(dependencia)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi dependencia es en {7} y tengo un título profesional en {8}.'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__dependencia(), self.get__tituloprofesion()))
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")


class Ops(Administrativos): 
    def _init_(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion="", numeses=0, valorcontrato=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion)
        self.__fechavinculacion=datetime.strptime(fechavinculacion, '%Y-%m-%d')
        self.__numeses=numeses
        self.__valorcontrato=valorcontrato
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__fechavinculacion(self):
        return self.__fechavinculacion
    

    def set__fechavinculacion(self, value):
        self.__fechavinculacion = datetime.strptime(value, '%d-%m-%Y')


    def get__numeses(self):
        return self.__numeses
    

    def set__numeses(self, value):
        self.__numeses = value


    def get__valorcontrato(self):
        return self.__valorcontrato
    

    def set__valorcontrato(self, value):
        self.__valorcontrato = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_administrativos(self): #Definiendo la función para leer los datos del administrador
        while True:
            dependencia =  str(input("Ingrese su lugar de dependencia: "))
            if (dependencia.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la dependencia
                self.set__dependencia(dependencia)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_numeses_contrato_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 3: #Unicamente si el valor ingresado es 3, se registrará como meses
                value = str(input("Ingrese los meses que trabaja: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un dato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 3, no lo acepta
                            print("No puede colocar un dato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__numeses(value) #Dato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 10: #Unicamente si el valor ingresado es 10, se registrará como valor de contrato
                value = str(input("Ingrese su valor de contrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__valorcontrato(value) #Valor aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi dependencia es en {7} y tengo un título profesional en {8}. Me vincularon el {9} con un trabajo de {10} meses, mi valor de contrato es de {11} y mi salario es de {12}'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__dependencia(), self.get__tituloprofesion(), self.get__fechavinculacion(),
               self.get__numeses(), self.get__valorcontrato(), self.get__salario()))
        
        
    def liquidarOPS(self): #Mostrando la liquidación TC
        print("Calculando la liquidación OPS...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")
        

class Planta(Administrativos): 
    def _init_(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion=""): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion)
        self.__fechavinculacion=datetime.strptime(fechavinculacion, '%Y-%m-%d')


    #Métodos getter y setter para los siguientes valores
    def get__fechavinculacion(self):
        return self.__fechavinculacion
    

    def set__fechavinculacion(self, value):
        self.__fechavinculacion = datetime.strptime(value, '%d-%m-%Y')


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_administrativos(self): #Definiendo la función para leer los datos del administrador
        while True:
            dependencia =  str(input("Ingrese su lugar de dependencia: "))
            if (dependencia.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la dependencia
                self.set__dependencia(dependencia)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi dependencia es en {7} y tengo un título profesional en {8}. Me vincularon el {9}.'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__dependencia(), self.get__tituloprofesion(), self.get__fechavinculacion()))
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")


class Auxiliar(Planta): 
    def _init_(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion, nivel=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion)
        self.__nivel=nivel
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__nivel(self):
        return self.__nivel
    

    def set__nivel(self, value):
        self.__nivel = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_administrativos(self): #Definiendo la función para leer los datos del administrador
        while True:
            dependencia =  str(input("Ingrese su lugar de dependencia: "))
            if (dependencia.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la dependencia
                self.set__dependencia(dependencia)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_nivel_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 2: #Unicamente si el valor ingresado es 2, se registrará como nivel
                value = str(input("Ingrese su nivel: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un nivel con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un nivel con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__nivel(value) #Nivel aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi dependencia es en {7} y tengo un título profesional en {8}. Me vincularon el {9} y mi nivel es de {10}'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__dependencia(), self.get__tituloprofesion(), self.get__fechavinculacion(),
               self.get__nivel()))
        
        
    def sueldo(self): #Mostrando el sueldo del docente
        print("Mi sueldo es de {0}".format(self.get__salario()))
        
        
    def liquidarAux(self): #Mostrando la liquidación Aux
        print("Calculando la liquidación auxiliar...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")
        

class Tecnico(Planta): 
    def _init_(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion, nivel=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion)
        self.__nivel=nivel
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__nivel(self):
        return self.__nivel
    

    def set__nivel(self, value):
        self.__nivel = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_administrativos(self): #Definiendo la función para leer los datos del administrador
        while True:
            dependencia =  str(input("Ingrese su lugar de dependencia: "))
            if (dependencia.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la dependencia
                self.set__dependencia(dependencia)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_nivel_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 2: #Unicamente si el valor ingresado es 2, se registrará como nivel
                value = str(input("Ingrese su nivel: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un nivel con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un nivel con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__nivel(value) #Nivel aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi dependencia es en {7} y tengo un título profesional en {8}. Me vincularon el {9} y mi nivel es de {10}'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__dependencia(), self.get__tituloprofesion(), self.get__fechavinculacion(),
               self.get__nivel()))
        
        
    def sueldo(self): #Mostrando el sueldo del docente
        print("Mi sueldo es de {0}".format(self.get__salario()))
        
        
    def liquidarTec(self): #Mostrando la liquidación Tec
        print("Calculando la liquidación técnico...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")
        

class Profesional(Planta): 
    def _init_(self, idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion, nivel=0, salario=0): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(idpersona, nombre, apellido, fechanacimiento, ciudadnacimiento, genero, estrato, dependencia, tituloprofesion, fechavinculacion)
        self.__nivel=nivel
        self.__salario=salario


    #Métodos getter y setter para los siguientes valores
    def get__nivel(self):
        return self.__nivel
    

    def set__nivel(self, value):
        self.__nivel = value


    def get__salario(self):
        return self.__salario
    

    def set__salario(self, value):
        self.__salario = value


    def leer_id_estrato(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 10: #Unicamente si el valor ingresado es 10, se registrará como documento
                value = str(input("Ingrese su número de identificación: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 10, no lo acepta
                            print("No puede colocar un documento con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__idpersona(value) #Documento aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 2: #Unicamente si el valor ingresado es 2, se registrará como estrato
                value = str(input("Ingrese su estrato: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un estrato con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un estrato con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__estrato(value) #Estrato aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def leer_nombre(self): #Definiendo la función para leer el nombre de la persona
        while True:
            nombre =  str(input("Ingrese su nombre: "))
            if (nombre.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el nombre
                self.set__nombre(nombre)
                while True: #Ahora pasará a aprobar el apellido
                    apellido =  str(input("Ingrese su apellido: "))
                    if (apellido.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el apellido
                        self.set__apellido(apellido)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_administrativos(self): #Definiendo la función para leer los datos del administrador
        while True:
            dependencia =  str(input("Ingrese su lugar de dependencia: "))
            if (dependencia.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba la dependencia
                self.set__dependencia(dependencia)
                while True: #Ahora pasará a aprobar el título profesional
                    titulo =  str(input("Ingrese su título profesional: "))
                    if (titulo.replace(" ","").isalpha()): #Si el dato ingresado son letras, aprueba el título
                        self.set__tituloprofesion(titulo)
                        break #Cerrando el ciclo
                    else: #Si el usuario ingresa números no las acepta.
                        print("Solo se permiten caracteres alfabéticos y espacios.") 
                break #Cerrando el ciclo
            else: #Si el usuario ingresa números no las acepta.
                print("Solo se permiten caracteres alfabéticos y espacios.")


    def leer_nivel_salario(self, min, max): #Definiendo la función para leer números
        while True:
            valor_aprobado = False
            if max == 2: #Unicamente si el valor ingresado es 2, se registrará como nivel
                value = str(input("Ingrese su nivel: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 1, no lo acepta
                            print("No puede colocar un nivel con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 2, no lo acepta
                            print("No puede colocar un nivel con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__nivel(value) #Nivel aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            elif max == 8: #Unicamente si el valor ingresado es 8, se registrará como salario
                value = str(input("Ingrese su salario: "))
                sol_num = Administrativos.solo_num(value)
                if sol_num == True:
                    while True:
                        if len(value) < min: #Si el valor es menor a 5, no lo acepta
                            print("No puede colocar un salario con una longitud inferior a {0}".format(min))
                            break
                        elif len(value) > max: #Si el valor es mayor a 8, no lo acepta
                            print("No puede colocar un salario con una longitud mayor a {0}".format(max))
                            break
                        else:
                            self.set__salario(value) #Salario aprobado
                            valor_aprobado = True
                            break #Rompiendo el ciclo
                else: #Si el usuario ingresa letras no las acepta.
                    print("Solo puede digitar caracteres numericos.")
            if valor_aprobado == True:
                break #Cerrando el ciclo


    def informacion(self): #Mostrando la información con .format
        print( 'Mi documento es {0}, me llamo {1} {2}. Nací el {3} en la ciudad de {4}, soy {5} y soy de estrato {6}. Mi dependencia es en {7} y tengo un título profesional en {8}. Me vincularon el {9} y mi nivel es de {10}'.format
              (self.get__idpersona(), self.get__nombre(), self.get__apellido(), self.get__fechanacimiento(), self.get__ciudadnacimiento(), self.get__genero(), self.get__estrato(), self.get__dependencia(), self.get__tituloprofesion(), self.get__fechavinculacion(),
               self.get__nivel()))
        
        
    def sueldo(self): #Mostrando el sueldo del docente
        print("Mi sueldo es de {0}".format(self.get__salario()))
        
        
    def liquidarProf(self): #Mostrando la liquidación Prof
        print("Calculando la liquidación profesional...")
        
        
    def mostrar_dg(self): #Mostrando el DG
        print("Mostrando el DG...")
        
    
    def calcular_eps(self): #Calculando EPS
        print("Calculando la EPS...")
        
        
    def calcular_pension(self): #Calculando pension
        print("Calculando la pension...")
        
        
    def calcular_arl(self): #Calculando ARL
        print("Calculando la ARL...")
        
        
    def calcular_sena(self): #Calculando el porcentaje SENA
        print("Calculando el porcentaje SENA...")
        
        
    def calcular_cajas(self): #Revisando las cajas
        print("Revisando las cajas...")
        
        
    def calcular_icbf(self): #Calculando el ICBF
        print("Calculando el ICBF...")
        
        
    def calcular_auxilio(self): #Calculando el auxilio
        print("Calculando auxílio...")


