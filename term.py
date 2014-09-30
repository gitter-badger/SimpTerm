'SimpTerm'
class AppInfo():
    version = "1.0.0.0"
class Configuration():
    init_onstartup = False
app = AppInfo()
config = COnfiguration()
def init():
    print("SimpTerm v" + app.version)
    print()
    print("")
    term()
def term():
    term_input = input("$>")
def read_config():
    if config.init_onstartup == True: init()
    else: term()
read_config()