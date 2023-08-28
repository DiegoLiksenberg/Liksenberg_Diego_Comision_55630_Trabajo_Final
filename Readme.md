# Proyecto Final Coderhouse - Curso de Python
Comisión: 55630
Alumno: Diego Esteban Liksenberg

## Nombre del Proyecto
Clubes Deportivos de la Ciudad de Córdoba

Versión
1.0

## Descripción del Proyecto
Página Web destinada a personas o usuarios que deseen realizar actividades deportivas en la ciudad de Córdoba.
Podrán conocer los diferentes clubes disponibles, los deportes a practicar y quiénes son los entrenadores y deportistas inscriptos.

Con el objeto de poder navegar por las distintas secciones de la página web, el usuario deberá iniciar sesión o bien registrarse en caso de no contar aún con un usuario y contraseña inscripto. En ambos casos, una vez que la página valide la autenticación del usuario, el mismo será redirigido al inicio de la página web.

Los usuarios podrán realizar las siguientes acciones:

- Visualizar todos los clubes existentes para hacer actividades deportivas, todos los deportes que se pueden practicar, los entrenadores disponibles y los deportistas inscriptos
- Agregar deportes, deportistas, entrenadores y clubes
- Eliminar deportes, deportistas, entrenadores y clubes
- Modificar los datos de los deportes, deportistas, entrenadores y clubes
- Buscar o filtrar entre los mismos en función del patrón que se busque. Para ello hay que ingresar a:
  a. Deporte: http://127.0.0.1:8000/buscar_deporte/
  b. Deportista: http://127.0.0.1:8000/buscar_deportista/
  c. Entrenador: http://127.0.0.1:8000/buscar_entrenador/
  d. Club: http://127.0.0.1:8000/buscar_club/
- Editar el perfil de Usuario 
- Cambiar la contraseña de Usuario
- Elegir un Avatar que represente al usuario si lo deseara en: http://127.0.0.1:8000/agregar_avatar/
- Cerrar Sesión
- Realizar Login en caso de haber cerrado la sesión
- Efectuar el registro del usuario

Los Modelos y Atributos utilizados son:

Deporte
 - nombre
 - categoría

Deportistas
 - nombre
 - apellido
 - email
 - edad

Entrenadores
 - nombre
 - apellido
 - email
 - edad
 - Fecha de Alta como entrenadores

Clubes
 - nombre
 - domicilio

**Los datos del usuario administrador son los siguientes:**
Usuario: admin
Contraseña: *Coderhouse

**Tecnología Utilizada:**

- Front-End
- HTML 5
- CSS 
- Javascript 
- Bootstrap 5.2.3

Back-End
- Python 3.11.4
- Django 4.2.3

**Pruebas Realizadas**
Ver archivo titulado "Casos de Test.xlsx" el cual se encuentra en el presente repositorio

**Video Demostración: Se encuentra en el presente repositorio y en la siguiente dirección de Youtube:**
https://www.youtube.com/watch?v=4flGwEOL_j8