
from conexion import Conexion
from persona import Persona
from logger_base import log
from persona_dao import PersonaDao

opcion = None
while opcion != 5:
    try:
        print('''
         ------Base de Datos, registro de personas ------
        presione 1: para Visualizar datos.
        presione 2: para Insertar datos.
        presione 3: para Actualizar datos.
        Presione 4: para Eliminar datos. 
        presiones 5: para Salir.  

         ''')

    
        opcion = int(input('Escribe tu opcion de (1-5):'))
        if opcion == 1:
            personas = PersonaDao.seleccionar()
            for persona in personas:
                log.debug(persona)
            opcion = None

        elif opcion == 2:
            nombre1 = input('Introduzca el nombre de persona:')
            apellido1 = input('Introduzca el apellido de persona:')
            email1 = input('Introduzca el email:')
            persona1 = Persona(nombre=nombre1, apellido=apellido1, email= email1)
            personas_insertadas = PersonaDao.insertar(persona1)
            log.debug(f'Personas insertadas: {personas_insertadas}')
        
            opcion = None
    
        elif opcion == 3:
            id_persona = int(input('Introduzca ID de persona:'))
            nombre = input('Introduzca el nombre de persona:')
            apellido = input('Introduzca el apellido de persona:')
            email = input('Introduzca el email:')
            persona2 = Persona(id_persona, nombre, apellido, email)
            persona_actualizados = PersonaDao.actualizar(persona2)
            log.debug(f'Personas actualizados: {persona_actualizados}')
            opcion = None

        elif opcion == 4:
            id_persona = int(input('Introduzca ID de persona:'))
            persona3 = Persona(id_persona)
            personas_eliminadas = PersonaDao.eliminar(persona3)
            log.debug(f'Personas eliminadas: {personas_eliminadas}')
            opcion = None
        
        
            
            
    
    except Exception as e:
        print(f'Ocurrio un error, se hizo rollback: {e}')
    
else:
    print('Salimos del programa')




