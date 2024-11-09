class Usuario:
    def __init__(self,id=None, nombre=None, apellido=None, dni=None, logueo=None, contraseña=None, id_datosprivados=None):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.logueo=logueo
        self.contraseña=contraseña
        self.id_datosprivados=id_datosprivados


#CONEXIÓN CON LA BASES DE DATOS
#consulta para agregar un campo
query_receta='''INSERT INTO usuario (nombre,apellido,dni,logueo,contraseña,id_datosprivados)
                        values(%s,%s,%s,%s,%s,%s)'''

cursor.execute(query_usuario,(usuario['Nombre'],usuario['Preparacion'],receta['Imagen'],receta['Tiempo_preparacion'],
                                        usuario['Tiempo_coccion'],usuario['Favorita']))  
            conn.commit() #guarda los datos


#me relaciona las dos tablas
#ultimo_id = cursor.lastrowid solo para la tabla de datos personales porque ahi comienza la relacion de datos
# ultimo_id = cursor.lastrowid 