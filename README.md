# Pyting Speed Test

Es, en simples palabras, un medidor de velocidad de tipeo teniendo en cuenta los fallos para dar un informe con precisión.

## Ejecución

Para comenzar la ejecución del proyecto se debe iniciar el documento main por medio de:

##### El terminal (recomendado):

<a href="https://imgur.com/DNJGufz"><img src="https://i.imgur.com/DNJGufz.png" title="source: imgur.com" /></a>


## Primer Lanzamiento
Al iniciar el documento main este va a generar una ventana:

<a href="https://imgur.com/fUu33ws"><img src="https://i.imgur.com/fUu33ws.png" title="source: imgur.com" /></a>


Lo primero que llama nuestra atención es un cuadro de texto en el que se avisa de cargar un archivo para iniciar el test.

<a href="https://imgur.com/1rBwieo"><img src="https://i.imgur.com/1rBwieo.png" title="source: imgur.com" /></a>


Esto se debe hacer por medio del botón.

<a href="https://imgur.com/W4gRHQP"><img src="https://i.imgur.com/W4gRHQP.png" title="source: imgur.com" /></a>


Al cargar el archivo se abrirá su contenido en la ventana de texto.

<a href="https://imgur.com/LkzQ1WF"><img src="https://i.imgur.com/LkzQ1WF.png" title="source: imgur.com" /></a>

El texto que se logra ver debajo de la entrada de texto son los puntajes obtenidos anteriormente.

<a href="https://imgur.com/0B8YLOM"><img src="https://i.imgur.com/0B8YLOM.png" title="source: imgur.com" /></a>


Una vez llegado hasta este momento, apenas se comience a escribir la barra superior comenzará a decrecer.

<a href="https://imgur.com/AKdmwCA"><img src="https://i.imgur.com/AKdmwCA.png" title="source: imgur.com" /></a>


Cuando la barrita se termine de consumir (al cabo de 1 minuto), se desplegará una ventana mostrando los resultados.

<a href="https://imgur.com/GdlzOSV"><img src="https://i.imgur.com/GdlzOSV.png" title="source: imgur.com" /></a>


Debajo de los resultados se encuentra una entrada de texto, donde se puede ingresar el nombre de la persona que tomó el test, consiguiente a la entrada de texto se encuentra el botón que guardará los datos del resultado obtenido.

<a href="https://imgur.com/hO0ybFw"><img src="https://i.imgur.com/hO0ybFw.png" title="source: imgur.com" /></a>


# Metodología

**“coreWindow.py”**: Este archivo contiene a la clase coreWindow, además de funcionar como un "main" ya que al final de la construcción de la clase se hace llamado de la misma.

**Clase "coreWindow"**: Esta clase es la clase "núcleo" ya que la gran parte de los métodos ocurren en esta clase, esta clase incorpora los siguientes métodos:
 + ***"loadFile"*** Este método es llamado por el botón con el icono de "crear una nueva ventana" en la parte superior izquierda.
 
 + ***"restart"*** Este método, accionado por el símbolo de parar activa la entrega de resultados, se considerará 1 minuto de igual formas, el botón tiene mayor función como DEBUG.
  
 + ***"start"*** Este método, accionado por los cambios dentro del entry, inicia la cuenta regresiva además de llevar un informe de las teclas escritas y las teclas correctas.

 + ***"entryInput"*** Este método es activado cuando la entrada de texto cambia, esto para actualizar la traducción de manera automática. Además esta detecta, por medio del label del título que se encuentra arriba de la misma, en qué modo se encuentra el proyecto, en el caso de que el modo sea morse y la entrada detecte un carácter que no pertenezca a los símbolos usados en el morse ".-/" mostrará un mensaje de recordatorio.

 + ***"onTimeOut"*** Este método es activado constantemente y está vinculado a la barra de "des-carga" acciona la muestra del resultado cuando se acaba el tiempo y es forzada al accionar el *reset*.

 + ***"displayResult"*** Desplega la ventana con los resultados del test.
 
 + ***"udpateScoreBoard"*** Actualiza los datos mostrados de los resultados anteriores.

**Clase "Results"**: Como indica su nombre, es la ventana de los resultados, esta no posee métodos, ya que su función es únicamente mostrar los datos recolectados en el test anterior. 

 + ***"saveResult"*** Guarda los datos en el archivo scoreBoard.


## Desarrollado por:
- Angel Guerrero
- Yostin Sepulveda

