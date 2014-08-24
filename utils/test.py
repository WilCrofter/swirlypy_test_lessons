from tkinter import *
from idlelib.EditorWindow import fixwordbreaks, EditorWindow
 
def edle(filename):
    root = Tk()
    fixwordbreaks(root)
    root.withdraw()
    edit = EditorWindow(root=root, filename=filename)
    edit.set_close_hook(root.quit)
    edit.text.bind("<<close-all-windows>>", edit.close_event)
    root.mainloop()
    root.destroy()
    
def hasIdle():
    """Returns True if the Idle editor is available, else False."""
    try:
        from idlelib.EditorWindow import EditorWindow
        return True
    except Exception:
        return False

