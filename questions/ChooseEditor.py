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
# 4. Check for presence of choice (?how)
# 5. Verify with test.


import shutil
# make a list of os-specific editors
eds = ("emacs", "vi", "nano", "pico", "gedit")
res = set(shutil.which(x) for x in eds)
