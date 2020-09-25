# W6-Project---The-Ranking
Weekly project "The Ranking"


![ironhack.jpeg](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/ironhack.jpeg)


El objetivo de este proyecto es crear un api que se nutra de una base de datos con la información de las pull request realizadas hasta la fecha. Esta base de datos ha sido obtenida de Github a través de su propia apikey.  


## Análisis.

Se ha creado un api que se encarga de realizar las siguientes acciones:

- Crear un nuevo estudiante.
- Consultar todos los estudiantes que han realizado pull requests a lo largo del presente bootcamp.
- Crear un nuevo lab.
- Análisis estadístico de un determinado lab.
- Obtener meme aleatorio de los enviados en un determinado lab hasta la fecha.


## Como se ha realizado.
 
 Como se ha indicado anteriomente, se ha importado la base de datos desde Github a través de su api, y para ello hemos tenido que generar un token. Una vez obtenidos los datos necesarios para el enrequicimiento de nuestra base de datos, hemos generado un json que hemos importado a MongoDB. 
 
 Posteriormente, hemos creado nuestra propia api, la cual se encarga de realizar las acciones arriba indicadas.


## Instrucciones de uso.

### Creación de un nuevo estudiante.

Para crear un nuevo estudiante se debe introducir la siguiente ruta:

    - http://localhost:3000/student/create/<studentname>

en el espacio reservado <studentname> debemos introducir el nombre del estudiante que queremos incluir en nuestra base de datos. En caso de que no se incluya ningún alumno, nuestra api nos devolverá la siguiente pantalla.

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.38.41.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/student-create/Captura%20de%20pantalla%202020-09-25%20a%20las%200.38.41.png)

Si hemos introducido con éxito el nuevo estudiante, nuestra api se encargará de devolvernos la siguiente pantalla y generar el estudiante dentro de la base de datos.
    
![Captura%20de%20pantalla%202020-09-25%20a%20las%200.40.11.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/student-create/Captura%20de%20pantalla%202020-09-25%20a%20las%200.40.11.png)

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.40.38.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/student-create/Captura%20de%20pantalla%202020-09-25%20a%20las%200.40.38.png)


### Consultar todos los estudiantes que han realizado pull requests a lo largo del presente bootcamp.

Para realizar esta consulta debemos introducir la siguiente ruta:

    - http://localhost:3000/student/all

Nuestra api se encargará de devolvernos una lista con todos los estudiantes.

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.41.06.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/all-students/Captura%20de%20pantalla%202020-09-25%20a%20las%200.41.06.png)


### Creación de un nuevo lab.

Para crear un nuevo lab se debe introducir la siguiente ruta:

    - http://localhost:3000/lab/create/<lab_name>

en el espacio reservado <lab_name> debemos introducir el nombre del lab que queremos incluir en nuestra base de datos. En caso de que no se incluya ningún lab, nuestra api nos devolverá la siguiente pantalla.

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.13.40.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/lab-create/Captura%20de%20pantalla%202020-09-25%20a%20las%200.13.40.png)

Si hemos introducido con éxito el nuevo lab, nuestra api se encargará de devolvernos la siguiente pantalla y generar el lab dentro de la base de datos.
    
![Captura%20de%20pantalla%202020-09-25%20a%20las%200.24.59.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/lab-create/Captura%20de%20pantalla%202020-09-25%20a%20las%200.24.59.png)

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.30.13.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/lab-create/Captura%20de%20pantalla%202020-09-25%20a%20las%200.30.13.png)


### Análisis estadístico de un determinado lab.

Para consultar las estadísticas de un determinado lab se debe introducir la siguiente ruta:

    - http://localhost:3000/lab/<lab_name>/search

en el espacio reservado <lab_name> debemos introducir el nombre del lab que queremos consultar. Nuestra api nos devuelve un análisis de la misma con los siguientes datos:

    1) Pull requests abiertas.
    2) Pull requests cerradas.
    3) % de pull request cerradas.
    4) Lista de estudiantes que han realizado cada pull request.
    5) Lista de memes en cada pull request.
    6) Notas de cada estudiante en cada pull request.

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.36.24.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/lab-analysis/Captura%20de%20pantalla%202020-09-25%20a%20las%200.36.24.png)


### Obtener meme aleatorio de un determinado lab.

Para obtener el enlace a un meme de un determinado lab se debe introducir la siguiente ruta:

    - http://localhost:3000/lab/<lab_name>/meme
    
En el espacio reservado <lab_name> debemos introducir el nombre del lab del que queremos obtener un meme aleatorio. Nuestra api nos devuelve el enlace de dicho meme.

![Captura%20de%20pantalla%202020-09-25%20a%20las%200.36.24.png](https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/img/random%20meme/Captura%20de%20pantalla%202020-09-25%20a%20las%200.37.57.png)
