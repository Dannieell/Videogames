PROYECTO INDIVIDUAL - DANIEL GOMERO
PL-ML-OPS

El presente proyecto trata sobre la creación de una API y su despliegue en RENDER. Sin embargo, toda la data aún está “sucia”, por lo que es necesario realizar los siguientes pasos:

- ETL
- EDA
- Funciones
- Crear API en FASTAPI
- Desplegar en RENDER
  
Los datos con los que se trabaja son los videos de la plataforma Steam. Estos datos se presentan en tres conjuntos de datos, cada uno con una serie de variables como ID, horas jugadas, años de lanzamiento, reseñas, géneros y otras categorías. El objetivo es desarrollar una función que pueda responder a las siguientes preguntas:

- Identificar el año con más horas jugadas para un género dado.
- Determinar el usuario que ha acumulado más horas jugadas en un género específico.
- Obtener el top 3 de juegos MÁS recomendados por los usuarios.
- Obtener el top 3 de juegos MENOS recomendados por los usuarios.
- Contabilizar la cantidad de registros de reseñas de usuarios.
- Recibir el ID de un producto y devolver una lista con 5 juegos recomendados similares.
- Recibir el ID de un usuario y devolver una lista con 5 juegos recomendados para dicho usuario.

1. ETL

Para este proceso, fue necesario desanidar los conjuntos de datos que estaban en formatos JSON. Se crearon tres notebooks de ETL, cada uno destinado a desanidar los tres conjuntos de datos. En este proceso, se convirtieron en dataframes y luego se guardaron en archivos CSV.

2. EDA
   
Una vez que los datos puedan ser utilizados, se realiza un proceso de depuración de los datos. Se eliminaron las columnas que no son necesarias para el análisis, con el objetivo de optimizar los recursos. El resultado son tres archivos CSV:

- Steam_games_eda.csv: Contiene todos los IDs, nombres de juegos, años de lanzamiento y género.
- User_items_eda.csv: Contiene las horas jugadas, el User_id y los IDs.
- User_review_eda.csv: Contiene las reseñas, IDs, User_id y años de las reseñas.

Para ello, se llevó a cabo la estrategia de unir los dataframes de manera que se obtengan dos dataframes únicos: items_games y review_games. Esto se hizo con el objetivo de optimizar recursos, como por ejemplo, que en las consultas de RENDER no ocupen mucho espacio, minimizar tiempos, realizar correcciones rápidas, etc.

3. Funciones
   
Se realizó un notebook previo al levantamiento de la API para verificar la lógica del código. Una vez comprobado que el código funciona, se creó el archivo .py con sus respectivos decoradores para la API.

4. FASTAPI
   
Se creó la API con el siguiente proceso: Se creó un entorno virtual donde se pudo trabajar la API a nivel local, se comprobó la funcionalidad de la API constantemente con el archivo .py y se descargaron las librerías a utilizar en el mismo entorno.

5. RENDER
Si se han realizado correctamente los pasos anteriores, RENDER debería funcionar sin problemas. Esta herramienta trabaja directamente con el repositorio y, al agregar el requirements.txt correctamente, cualquier persona puede conectarse con nuestro 'web service'.



link Render: https://videogames-pruh.onrender.com/docs
link Youtube: https://www.youtube.com/watch?v=2yDkn91ImRg
link Github: https://github.com/Dannieell/Videogames
