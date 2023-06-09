from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool


class PersonaDao:
    '''
    DAO (Data Access Object)
    CRUD (Created-Read-Update-Delete)

    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM persona WHERE  id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
   
    #Actualizar un registro
    persona2 = Persona(10, 'Daniel', 'Rodriguez', 'DR@gmail.com')
    persona_actualizados = PersonaDao.actualizar(persona2)
    log.debug(f'Personas actualizados: {persona_actualizados}')
    



    # Selecionar objetos
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)


