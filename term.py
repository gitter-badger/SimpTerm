'SimpTerm'
import subprocess
class AppInfo():
    version = "1.0.0.0"
class Configuration():
    init_onstartup = False
app = AppInfo()
config = Configuration()
def init():
    print("SimpTerm v" + app.version)
    print()
    print("")
    term()
def term():
    term_input = input("$>")
    if term_input == "": term()
    elif term_input == "about": About()
    else:
        subprocess.Popen(term_input)
        term()
def About():
    print("SimpTerm v" + app.version)
def read_config():
    if config.init_onstartup == True: init()
    else: term()
'Reads the configuration'
read_config()