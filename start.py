import getpass as gt
import subprocess
import sys
import os
from colorama import init, Fore, Back, Style

from System.Win import check_git_version
from System.Linux import check_git_version, check_brew_version
from System.Mac import check_git_version, check_brew_version

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

oprendszer = sys.platform


global system_os
global applist

if oprendszer.startswith('win'):
    #windows
    system_os = oprendszer
    # downloads
    applist = ('Notepad++', 'Qbittorent')


elif oprendszer.startswith('linux'):
    #linux
    system_os = oprendszer
    applist = ('htop', 'nc', 'qbittorent')


elif oprendszer.startswith('darwin'):
    #macos
    system_os = oprendszer
    applist = ('htop', '34t34t', 'asassa')


else:
    #not detected system
    pass

init()
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL





print(Fore.GREEN +'------------------------------------------'+ Fore.RESET)
print(Fore.RED +'            Hello ' + Fore.MAGENTA + gt.getuser()+ Fore.RESET)
print(Fore.GREEN +'      *** Script start ' + system_os + ' ***'+ Fore.RESET)
print(Fore.GREEN +'------------------------------------------'+ Fore.RESET)

print(Fore.GREEN + 'GIT:' + Fore.RESET + check_git_version())
print(Fore.GREEN + 'BREW:' + Fore.RESET + check_brew_version())
print(Fore.RED + 'DOWNLOADS APP LIST' + Fore.RESET)

install_list = []  # Üres lista a telepítendő alkalmazásoknak

for app in applist:
    install = input(
        'Szeretnéd telepíteni a következő alkalmazást:' + Fore.CYAN + f'  {app}?' + Fore.RESET + ' (y/n) ')
    if install.lower() == 'y':
        install_list.append(app)

print(f'A telepítendő alkalmazások: {install_list}')

for app in applist:
    if app in install_list:
        print(Fore.GREEN + f'Telepítés: {app}')
    else:
        print(Fore.RED + f'Nem telepítendő: {app}')



if oprendszer.startswith('win'):
    #windows
    print('asdasd')


elif oprendszer.startswith('linux'):
    #linux
    if 'htop' in install_list:
        print('asdasdasd')


elif oprendszer.startswith('darwin'):
    #macos
    if 'htop' in install_list:
        parancs = "brew install htop"
        subprocess.Popen(['osascript', '-e', 'tell app "Terminal" to do script "' + parancs + '"'])

else:
    #not detected system
    pass


print(Style.RESET_ALL)









