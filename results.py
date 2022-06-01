from cProfile import label
import gi
from matplotlib import container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Results(Gtk.Window):
    def __init__(self, parent):
        super().__init__(title="¡¡¡ Felicidades !!!")
        self.set_resizable(False)
        self.set_default()

        self.core = parent

        #self.set_default_size(150, 100)

        # Imagen
        img_snail = Gtk.Image().new_from_file("res/caracol.png")
        img_trex = Gtk.Image().new_from_file("res/trex.png")
        img_monkey = Gtk.Image().new_from_file("res/monkey.png")
        img_octopus = Gtk.Image().new_from_file("res/octopus.jpg")
        img_cheetah = Gtk.Image().new_from_file("res/cheetah.png")

        #Calculo de nivel de velocidad

        if parent.words <= 20:
            img_grade = img_snail
            grade = "Eres un Caracol"
            self.resultGrade = "Caracol"

        if (parent.words > 20) and (parent.words <= 40):
            img_grade = img_trex
            grade = "Eres un T-Rex"
            self.resultGrade = "T-Rex"

        if (parent.words > 40) and (parent.words <= 60):
            img_grade = img_monkey
            grade = "Eres un Mono"
            self.resultGrade = "Mono"

        if (parent.words > 60) and (parent.words <=70):
            img_grade = img_octopus
            grade = "Eres un Pulpo"
            self.resultGrade = "Pulpo"

        if parent.words > 70:
            img_grade = img_cheetah
            grade = "Eres un Leopardo"
            self.resultGrade = "Leopardo"

        #Calculo de palabras por minuto
        self.realWords = str(parent.words)
        wpm = self.realWords + " palabras por minuto"

        #Calculo de precision
        self.acuracy = str(round(((parent.points*100)/parent.letters),2)) + "%"
        acuracyLBL = self.acuracy + " de precisión"

        #Calculo de proporcion
        prop = str(parent.points) + " / " + str(parent.letters)

        # Labels
        lbl_grade = Gtk.Label(label = grade)
        lbl_wpm = Gtk.Label(label = wpm)
        lbl_precision = Gtk.Label(label = acuracyLBL)
        lbl_proportion = Gtk.Label(label = prop)

        # Entry - Nombre del testeado
        self.ent_userName = Gtk.Entry()
        self.ent_userName.set_placeholder_text("Ingrese su nombre aquí")

        # Button - Confirmar guardado de los resultados
        btn_saveResult = Gtk.Button(label = "Guardar resultado")
        btn_saveResult.connect("clicked", self.saveResult)


        # Contenedor de los labels de información
        infoBox = Gtk.Box()
        infoBox.set_orientation(Gtk.Orientation.VERTICAL)

        infoBox.pack_start(lbl_grade, True, True, 0)
        infoBox.pack_start(lbl_wpm, True, True, 0)
        infoBox.pack_start(lbl_precision, True, True, 0)
        infoBox.pack_start(lbl_proportion, True, True, 0)

        # Contenedor info de la tabla de resultados
        boardBox = Gtk.Box()
        boardBox.set_orientation(Gtk.Orientation.HORIZONTAL)

        boardBox.pack_start(self.ent_userName, True, True, 0)
        boardBox.pack_start(btn_saveResult, True, True, 0)

        # Contenedor Principal para organizar los widgets de información
        resultBox = Gtk.Box()
        resultBox.set_orientation(Gtk.Orientation.HORIZONTAL)

        resultBox.pack_start(img_grade, True, True, 30)
        resultBox.pack_start(infoBox, True, True, 30)

        # Contenedor principal
        mainBox = Gtk.Box()
        mainBox.set_orientation(Gtk.Orientation.VERTICAL)
        
        mainBox.pack_start(resultBox, True, True, 30)
        mainBox.pack_start(boardBox, True, True, 30)

        self.add(mainBox)

        self.show_all()

    def saveResult(self, widget):
        if self.ent_userName.get_text() == "":
            self.ent_userName.set_placeholder_text("Debes ingresar un nombre de usuario")

        else:
            scoreBoard = open("res/scoreboard", "a")


            espaciado_nombre = 10-len(self.ent_userName.get_text())
            str_username = self.ent_userName.get_text() + espaciado_nombre*" " + "|"
            
            espaciado_grado = 10-len(self.resultGrade)
            str_grade = self.resultGrade + espaciado_grado*" "+"|"

            espaciado_palabras = 9 - len(self.realWords)
            str_words = self.realWords + espaciado_palabras*" "+"|"

            scoreBoard.write("\n"+str_username + str_grade + str_words + self.acuracy)
            
            
            scoreBoard.close()
            self.core.udpateScoreBoard()
            self.destroy()
