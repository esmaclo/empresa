__author__ = 'Esmir Acosta'

class Empresa():
    """
    Clase que representa un empleado
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        Metodo constructor de la clase Empresa

        Se inicializaran 3 atributos con los parametros pasados y aparte se creara una lista de departamentos vacia.

        :param nombre_empresa: Nombre de la empresa.
        :type nombre_empresa: str
        :param cif: Cif de la empresa
        :type cif: str
        :param razon_social: Razon social de la empresa.
        :type razon_social: str
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.departamentos = []

