import server.server_script as srv
import interfaces.election_committee_ui as ik
#import interfaces.voter as client
import interfaces.client_ui as desktop
import sys


if __name__ == '__main__':
    ik.ik_main()
    #client.voter_main()
    #srv.server_main()
    # app = desktop.QtWidgets.QApplication(sys.argv)
    # MainWindow = desktop.QtWidgets.QMainWindow()
    # ui = desktop.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
