#Start for terminal Apple Script

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

parancs = "clear &&" + "python3 " + dname +"/start.py"
os.system('osascript -e \'tell app "Terminal" to do script "' + parancs + '"\'')