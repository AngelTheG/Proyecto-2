# Pyting Speed Test

Es, en simples palabras, un medidor de velocidad de tipeo teniendo en cuenta los fallos para dar un informe con precisión.

## Ejecución

Para comenzar la ejecución del proyecto se debe iniciar el documento main por medio de:

##### El terminal (recomendado):

[===========Imagen=============]


## Primer Lanzamiento
Al iniciar el documento main este va a generar una ventana:
[===========Imagen=============]


Lo primero que llama nuestra atención es un cuadro de texto en el que se avisa de cargar un archivo para iniciar el test.
[===========Imagen=============]


Esto se debe hacer por medio del botón.
[===========Imagen=============]


Al cargar el archivo se abrirá su contenido en la ventana de texto.
[===========Imagen=============]


Una vez llegado hasta este momento, apenas se comience a escribir la barra superior comenzará a decrecer.
[===========Imagen=============]


Cuando la barrita se termine de consumir (al cabo de 1 minuto), se desplegará una ventana mostrando los resultados.
[===========Imagen=============]


# Metodología

**“coreWindow.py”**: Este archivo contiene a la clase coreWindow, además de funcionar como un "main" ya que al final de la construcción de la clase se hace llamado de la misma.

**Clase "coreWindow"**: Esta clase es la clase "núcleo" ya que la gran parte de los métodos ocurren en esta clase, esta clase incorpora los siguientes métodos:
 + ***"loadFile"*** Este método es llamado por el botón con el icono de "crear una nueva ventana" en la parte superior izquierda.
 
 + ***"restart"*** Este método, accionado por el símbolo de parar activa la entrega de resultados, se considerará 1 minuto de igual formas, el botón tiene mayor función como DEBUG.
  
 + ***"start"*** Este método, accionado por los cambios dentro del entry, inicia la cuenta regresiva además de llevar un informe de las teclas escritas y las teclas correctas.

 + ***"entryInput"*** Este método es activado cuando la entrada de texto cambia, esto para actualizar la traducción de manera automática. Además esta detecta, por medio del label del título que se encuentra arriba de la misma, en qué modo se encuentra el proyecto, en el caso de que el modo sea morse y la entrada detecte un carácter que no pertenezca a los símbolos usados en el morse ".-/" mostrará un mensaje de recordatorio.

 + ***"onTimeOut"*** Este método es activado constantemente y está vinculado a la barra de "des-carga" acciona la muestra del resultado cuando se acaba el tiempo y es forzada al accionar el *reset*.

 + ***"displayResult"*** Desplega la ventana con los resultados del test.

**Clase "Results"**: Como indica su nombre, es la ventana de los resultados, esta no posee métodos, ya que su función es únicamente mostrar los datos recolectados en el test anterior. 


## Desarrollado por:
- Angel Guerrero
- Yostin Sepulveda

