# The point is to find an editor.
# Some common editors follow. I'll probably hard-code the most common
# and allow a user to enter a custom choice.
# 
#~ gedit = GNOME  
#~ Leafpad = LXDE, Xfce 
#~ Kate = KDE

#~ Notepad = Windows 
#~ Notepad++ = Windows

#~ SimpleText = Mac OS
#~ TextEdit = OS X

#~ emacs = linux
#~ vi(m) = linux
#~ nano = linux
#~ pico = linux

# 1. Check the $EDITOR environmental variable
# 2. In its absence present a list based on os, and including other
# 3. If other, enter name.
# 4. Check for presence of choice (shutil.which)
# 5. Verify with test.


import shutil
# make a list of os-specific editors
eds = ("emacs", "vi", "nano", "pico", "gedit")
res = set(shutil.which(x) for x in eds)

# How to tell if python is running in a terminal or a gui
import sys
sys.stdout.isatty()

# http://en.wikipedia.org/wiki/List_of_terminal_emulators

# Spawning vi in a new terminal
# gnome-terminal -x vi tst.py
# xterm -e vi tst.py
# konsole -e vi tst.py
# x-terminal-emulator -e vi tst.py # is supposed to be unix universal (not on AGB's arch installation, though xterm is)

