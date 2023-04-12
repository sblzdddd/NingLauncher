import subprocess
import sys
from modules.NLcorlib import *
from modules.WindowMain import *
from PyQt5 import QtWidgets

jre_path = 'jre-17.0.1/bin/java.exe'
minecraft_path = "./.minecraft"


def launch():
    core = NLCore()
    params = core.generate_params()
    subprocess.Popen(f"{jre_path} {params}")
    MW.ui.Status.setText("Game Launched")
    MW.ui.LaunchButton.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MW = WindowMain()
    # launch game
    MW.ui.LaunchButton.clicked.connect(launch)
    MW.ShowWindow(True)
    sys.exit(app.exec())
