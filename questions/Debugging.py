from swirlypy.questions.Recording import *

class DebuggingQuestion(RecordingQuestion):
     
    def test_response(self, response, data={}):
        """
        just prints responses and returns True.
        """
        if "ast" in response:
            print("\nast: ", ast.dump(response["ast"]))
        if "added" in response:
            print("\nadded: ", response["added"])
        if "changed" in response:
            print("changed: ", response["changed"])
        if "removed" in response:
            print("removed: ", response["removed"])
        if "values" in response:
            print("\nvalues: ", response["values"])
        if "traceback" in response:
            print("\ntraceback: ", response["traceback"])
        return response["traceback"] == None
        
    def execute(self, data={}):
        super().execute(data=data)
        print("coursedir: ", data["coursedir"])
 
