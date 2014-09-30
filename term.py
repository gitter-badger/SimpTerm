'SimpTerm'
import subprocess
class AppInfo():
    version = "1.0.0.0"
class Configuration():
    init_onstartup = False
    update_using_git = False
    wget_no_cert = False
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
    elif term_input == "exit": exit()
    elif term_input == "st -about": About()
    elif term_input == "st -update": Updates()
    else:
        subprocess.Popen(term_input)
        term()
def About():
    print("SimpTerm v" + app.version)
    term()
def Updates():
    print("SimpTerm v" + app.version)
    print()
    if config.update_using_git == True:
        print("Getting updates...")
        print("Fetching files... [0%]")
        subprocess.Popen("git clone https://github.com/deavmi/SimpTerm.git")
        print("Fetching files... [100%]")
        print("Update completed!")
    else:
        if config.wget_no_cert == True: flag = " --no-check-certificate"
        else: flag = ""
        print("Getting updates...")
        print("Fetching file [1 of 3]")
        subprocess.Popen("wget https://raw.githubusercontent.com/deavmi/SimpTerm/master/term.py" + flag)
        print("Fetching file [2 of 3]")
        subprocess.Popen("wget https://raw.githubusercontent.com/deavmi/SimpTerm/master/LICENSE" + flag)
        print("Fetching file [3 of 3]")
        subprocess.Popen("wget https://raw.githubusercontent.com/deavmi/SimpTerm/master/README.md" + flag)
        print("Update completed!")
    term()
def read_config():
    if config.init_onstartup == True: init()
    else: term()
'Reads the configuration'
read_config()