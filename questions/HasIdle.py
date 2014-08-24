from swirlypy.question import CategoryQuestion
from swirlypy.colors import print_err

class HasIdleQuestion(CategoryQuestion):
    """Checks whether or not IDLE is available, exiting with error if it is not.""" 
    
    def execute(self, data={}):
        try:
            from idlelib.EditorWindow import EditorWindow
        except Exception:
            print_err("This lesson requires IDLE. To proceed idlelib and its dependencies, tkinter and _tkinter, must be installed. Sorry for the inconvenience.")
            input("<enter> to leave swirlypy")
            sys.exit()


