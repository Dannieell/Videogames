Proyecto Individual - Daniel Gomero
PL-ML-OPS

El presente proyecto se centra en la creación de una API y su despliegue en RENDER. Sin embargo, la data aún no está procesada adecuadamente, por lo que se deben seguir los siguientes pasos:

- ETL (Extracción, Transformación y Carga de Datos)
- EDA (Análisis Exploratorio de Datos)
- Desarrollo de Funciones
- Creación de la API con FastAPI
- Despliegue en RENDER

La información con la que se trabaja son los datos de videojuegos de la plataforma Steam, los cuales se presentan en tres conjuntos de datos. Cada uno contiene una serie de variables como ID, horas jugadas, años de lanzamiento, reseñas, géneros y otras categorías. El objetivo es desarrollar funciones que puedan responder a las siguientes preguntas:

- Identificar el año con más horas jugadas para un género dado.
- Determinar el usuario que ha acumulado más horas jugadas en un género específico.
- Obtener el top 3 de juegos más recomendados por los usuarios.
- Obtener el top 3 de juegos menos recomendados por los usuarios.
- Contabilizar la cantidad de reseñas de usuarios siendo negativos o positivos
- Recibir el ID de un producto y devolver una lista con 5 juegos similares recomendados.
- Recibir el ID de un usuario y devolver una lista con 5 juegos recomendados para dicho usuario.

ETL
Para el proceso de Extracción, Transformación y Carga de Datos, se utilizaron tres notebooks diferentes, cada uno encargado de procesar un conjunto de datos JSON. En este proceso, se desanidaron los datos y se convirtieron en dataframes, los cuales luego se guardaron en archivos CSV.

EDA
Una vez que los datos están listos para su uso, se realiza un Análisis Exploratorio de Datos para depurar la información. Se eliminan las columnas innecesarias para el análisis, optimizando así los recursos. El resultado son tres archivos CSV: Steam_games_eda.csv, User_items_eda.csv y User_review_eda.csv.

Funciones
Se desarrollaron funciones previamente al levantamiento de la API para verificar la lógica del código. Una vez verificado su funcionamiento, se crearon los archivos .py con los decoradores correspondientes para la API.

FastAPI
La API se crea en un entorno virtual, donde se verifica su funcionalidad con el archivo .py y se instalan las bibliotecas necesarias en dicho entorno.

RENDER
Si se han seguido correctamente los pasos anteriores, RENDER debería funcionar sin problemas. Esta herramienta trabaja directamente con el repositorio y, al agregar el archivo requirements.txt correctamente, cualquier persona puede conectarse con nuestro servicio web.
