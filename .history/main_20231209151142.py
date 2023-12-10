from headers import *



class Application:
        """main Application"""
    def expection_handleing(self,e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        open("exceptions.log","a+").write(f"{str(exc_type)} :: {str(fname)} :: {str(exc_tb.tb_lineno)}\n")
        
    def msgbx(self,title,text):
        try:
            self.window.setEnabled(False)
            self.msgBox.setText(text)
            self.msgBox.setWindowTitle(title)
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
        except Exception as e:
            self.expection_handleing(e)
    def __init__(self):
    
        try:
            super().__init__()
            self.app = QtWidgets.QApplication(sys.argv)
            self.movie = QMovie("resources/mviis_loading.gif")
            self.splash = MovieSplashScreen(self.movie)
            self.window = Ui()
        except Exception as e:
           
            self.expection_handleing(e)