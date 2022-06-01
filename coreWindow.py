import gi
from matplotlib import container

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

from results import Results

class CoreWindow(Gtk.Window):
    def __init__(self):
        #Edición de la ventana principal
        super().__init__(title="Pyting Speed Test")
        self.set_border_width(50)
        self.set_size_request(800, 600)
        self.set_resizable(False)

        # Variables
        self.readyToGo = False
        self.unstarted = True
        self.restarted = False
        self.words = 0
        self.fileText = ""
        self.letters = 0
        self.points = 0
        self.wordRound = 0

        # Botón de carga de archivo
        btn_loadFile = Gtk.Button().new_from_icon_name("window-new", 6)
        btn_loadFile.connect("clicked", self.loadFile)

        # Barra de estado de tiempo
        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_fraction(1)

        # Botón reiniciar
        btn_restart = Gtk.Button().new_from_icon_name("process-stop", 6)
        btn_restart.connect("clicked", self.restart)

        # Textviewer texto seleccionado
        self.txt_test = Gtk.TextView()
        self.txt_test.set_editable(False)

        self.txt_test.get_buffer().set_text("Recuerda seleccionar un archivo de texto")

        # Entry de escritura
        self.ent_entry = Gtk.Entry()
        self.ent_entry.set_placeholder_text("El timer iniciará al comenzar a escribir")
        self.ent_entry.connect("changed", self.start)

        # Textviewer tablas de puntaje
        scroll = Gtk.ScrolledWindow()
        scroll.set_hexpand(True)
        scroll.set_vexpand(True)

        self.file_scoreBoard = open("res/scoreboard","r")

        self.scoreBoard = Gtk.TextView()
        self.scoreBoard.set_editable(False)
        self.scoreBoard.get_buffer().set_text(self.file_scoreBoard.read())
        self.file_scoreBoard.close()
        
        scroll.add(self.scoreBoard)
    
        # Grid para organizar de manera más personalizada los widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(110)
        grid.set_row_spacing(30)

        grid.attach(btn_loadFile, 0, 0, 1, 1)
        grid.attach_next_to(self.progressbar, btn_loadFile, Gtk.PositionType.RIGHT, 4, 1)
        grid.attach_next_to(btn_restart, self.progressbar, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.txt_test, self.progressbar, Gtk.PositionType.BOTTOM, 4,1)
        grid.attach_next_to(self.ent_entry, self.txt_test, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(scroll, self.ent_entry, Gtk.PositionType.BOTTOM,4,1)

        self.add(grid)
        

    def loadFile(self,widget):
        print("Seleción Archivo")

        # Nuevo
        dialog = Gtk.FileChooserDialog(title="Selecciona un archivo .txt", parent=self, action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL,
                           Gtk.ResponseType.CANCEL,
                           Gtk.STOCK_OPEN,
                           Gtk.ResponseType.OK)

        filter_text = Gtk.FileFilter()
        filter_text.set_name("Archivos de texto")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.fileText = ""
            print(" Archivo seleccionado - " + dialog.get_filename())
            self.file = open(dialog.get_filename())

        elif response == Gtk.ResponseType.CANCEL:
            print("Operación cancelada")
        
        textWord = ""
        self.textWords = []

        for sentence in self.file:
            for word in sentence:
                if (word != " ") and (word not in "\n"):
                    textWord += word

                if word == " ":
                    self.textWords.append(textWord)
                    textWord = ""

            self.fileText += sentence


        self.txt_test.get_buffer().set_text(self.fileText)

        self.readyToGo = True

        dialog.destroy()


    def restart(self,widget):
        if self.words > 0:
            self.restarted = True


    def start(self,widget):
        if self.readyToGo:
            if self.unstarted:
                    self.unstarted = False
                    self.timeout_id = GLib.timeout_add(600, self.on_timeout, None)
            
            # Detectar si la entrada está vacía
            if self.ent_entry != "":
                if " " in self.ent_entry.get_text():
                    
                    entryLetters = []
                    realLetters = []
                    for entryLetter in self.ent_entry.get_text():
                        entryLetters.append(entryLetter)

                    for realLetter in self.textWords[self.wordRound]:
                        realLetters.append(realLetter)
                        self.letters += 1

                    #Caso en el que la entrada es mas corta que la palabra original
                    if len(entryLetters) < len(realLetters):
                        i = 0
                        for letter in entryLetters:
                            if letter == realLetters[i]:
                                self.points += 1
                                i += 1

                    if len(entryLetters) > len(realLetters):
                        i = 0
                        for letter in realLetters:
                            if letter == entryLetters[i]:
                                self.points += 1
                                i += 1

                    if len(entryLetters) == len(realLetters):
                        i = 0
                        for letter in entryLetters:
                            if letter == realLetters[i]:
                                self.points += 1
                                i += 1


                    self.ent_entry.set_text("")
                    self.words += 1 

        if self.readyToGo == False:
            self.ent_entry.set_text("")

    def on_timeout(self, user_data):
        
        if self.restarted == True:

            # DEBUG - El botón de reset arroja resultados instantáneos
            self.displayResult()

            self.restarted = False
            self.words = 0
            self.progressbar.set_fraction(1)
            self.ent_entry.set_text("")
            self.unstarted = True
            return False

        else:
            new_value = self.progressbar.get_fraction() - 0.01
            
            if new_value <= 0:
                print("Jelou")
                self.progressbar.set_fraction(1)

                self.ent_entry.set_text("")
                self.unstarted = True
                self.displayResult()

                return False

            self.progressbar.set_fraction(new_value)
        return True


    def displayResult(self):
        Results(self)
        self.wordRound = 0

    def udpateScoreBoard(self):
        self.scoreBoard.get_buffer().set_text("")
        self.file_scoreBoard = open("res/scoreboard","r")
        self.scoreBoard.get_buffer().set_text(self.file_scoreBoard.read())
        self.file_scoreBoard.close()


#Run de la ventana principal
win = CoreWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()