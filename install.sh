echo "SimpTerm GNU/Linux Installer"
echo "=============================="
echo "Asking for root access..."
sudo bash
echo "Updating apt-get now..."
apt-get update
echo "Checking requirements..."
apt-get install git wget python
echo "Carrying on with installation..."
echo "Installing SimpTerm..."
echo "Changing directory to \bin ..."
cd \bin
echo "Cloning repository..."
git clone https://github.com/deavmi/SimpTerm.git
echo "Creating files..."
echo "py term.py" > st
echo "Installation completed! Launch SimpTerm with command 'st'. Have a great day forwards. :D"
echo "=============================="
