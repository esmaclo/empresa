__author__ = 'Esmir Acosta'

class Empleado():
    """
    Clase que representa un empleado
    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Metodo contructor de la clase Empleado

        Se inicializaran 7 atributos con los valores pasados como parametro

        :param nombre: Nombre del empleado
        :type nombre: str
        :param apellidos: Apellidos del empleado
        :type apellidos: str
        :param dni: DNI del empleado
        :type dni: str
        :param direccion: Direccion del empleado
        :type direccion: str
        :param edad: Edad del empleado
        :type edad: int
        :param email: Email del empleado
        :type email: str
        :param salario: Salario del empleado
        :type salario: int
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Metodo consultor del atributo salario

        Metodo que devuelve el valor del salario

        :return: Retorna el valor del atributo propio salario
        :rtype: int
        """
        return self.salario

    def get_dni(self):
        """
        Metodo consultor del atributo dni

        Metodo que devuelve el valor del dni

        :return: Retorna el valor del atributo propio dni
        :rtype: str
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Metodo consultor de los atributos nombre y apellidos

        Metodo que devuelve el valor del nombre y apellidos separados por espacio

        :return: Retorna el valor del atributo propio nombre y apellidos
        :rtype: str
        """
        return self.nombre + " " + self.apellidos

    def get_edad(self):
        """
        Metodo consultor del atributo edad

        Metodo que devuelve el valor de la edad

        :return: Retorna el valor del atributo propio edad
        :rtype: int
        """
        return self.edad

    def get_email(self):
        """
        Metodo consultor del atributo email

        Metodo que devuelve el valor del email

        :return: Retorna el valor del atributo propio email
        :rtype: str
        """
        return self.email

    def get_direccion(self):
        """
        Metodo consultor del atributo direccion

        Metodo que devuelve el valor de la direccion

        :return: Retorna el valor del atributo propio direccion
        :rtype: str
        """
        return self.direccion

    def get_salario_mensual(self):
        """
        Metodo que se encarga de calcular el salario mensual del empleado

        Sabiendo cual es el salario anual del empleado con el atributo propio salario, se calcula el mensual dividiendolo por 12

        :return: Retorna el salario mensual
        :rtype: int
        """
        return self.get_salario()/12
