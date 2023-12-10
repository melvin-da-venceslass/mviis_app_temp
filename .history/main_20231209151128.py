from headers import *



class Application:
    def __init__(self):
    
        try:
            super().__init__()
            self.app = QtWidgets.QApplication(sys.argv)
            self.movie = QMovie("resources/mviis_loading.gif")
            self.splash = MovieSplashScreen(self.movie)
            self.window = Ui()
        except Exception as e:
           
            self.expection_handleing(e)