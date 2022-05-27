from cProfile import label
import gi
from matplotlib import container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Results(Gtk.Window):
    def __init__(self, parent):
        super().__init__(title="¡¡¡ Felicidades !!!")

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

        if (parent.words > 20) and (parent.words <= 40):
            img_grade = img_trex
            grade = "Eres un T-Rex"

        if (parent.words > 40) and (parent.words <= 60):
            img_grade = img_monkey
            grade = "Eres un Mono"

        if (parent.words > 60) and (parent.words <=70):
            img_grade = img_octopus
            grade = "Eres un Pulpo"

        if parent.words > 70:
            img_grade = img_cheetah
            grade = "Eres un Leopardo"

        #Calculo de palabras por minuto
        wpm = str(parent.words) + " palabras por minuto"

        #Calculo de precision
        acuracy = (parent.points*100)/parent.letters
        acuracyLBL = str(acuracy) + "% de precisión"

        #Calculo de proporcion
        prop = str(parent.points) + " / " + str(parent.letters)

        # Labels
        lbl_grade = Gtk.Label(label = grade)
        lbl_wpm = Gtk.Label(label = wpm)
        lbl_precision = Gtk.Label(label = acuracyLBL)
        lbl_proportion = Gtk.Label(label = prop)

        # Contenedor de los labels de información
        infoBox = Gtk.Box()
        infoBox.set_orientation(Gtk.Orientation.VERTICAL)

        infoBox.pack_start(lbl_grade, True, True, 0)
        infoBox.pack_start(lbl_wpm, True, True, 0)
        infoBox.pack_start(lbl_precision, True, True, 0)
        infoBox.pack_start(lbl_proportion, True, True, 0)

        # Contenedor Principal para organizar los widgets
        mainBox = Gtk.Box()
        mainBox.set_orientation(Gtk.Orientation.HORIZONTAL)

        mainBox.pack_start(img_grade, True, True, 30)
        mainBox.pack_start(infoBox, True, True, 30)

        self.add(mainBox)

        self.show_all()
