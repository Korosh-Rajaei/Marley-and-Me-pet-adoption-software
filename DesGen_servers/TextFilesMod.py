import os.path
class TextFilesModClass:
    '''A class which opens, writes, searches, views and deletes descriptions in a text file.'''
    def OpenTextFile(self,path):
        if os.path.isfile(path):
            f = open(path)
            #print("Text file accessed!:\n")
            f.close()
            return True
        else:
            print("Text file does not exist!:\n")
            return False
    def WriteTextFile(self,text,path):
        if os.path.isfile(path):
            f = open(path,"a")
            f.write(text + "\n")
            f.close()
            #print("writing done!")
            return True
        else:
            print("Text file does not exist!:\n")
            return False
    def SearchTextFile(self,text,path):
        if os.path.isfile(path):
            f = open(path, "r")
            data = f.readlines()
            for i in data:
                if text in i:
                    # list2=i.split(" ||||| ")
                    s=i.replace("\n","")
                    f.close()
                    print("found the text/description!")
                    return s
            print("the text/description doesn't exist!")
            return False
        else:
            print("Text file does not exist!:\n")
            return False

    def EditingDescription(self,text,changed):
        output=text.replace(text,changed)
        return output
    def EditDescription(self,text,edited_text,path):
        if os.path.isfile(path):
            f = open(path,"r")
            s= f.read()
            f.close()
            chngdtext=s.replace(text,"")
            f = open(path,"w")
            f.write(chngdtext)
            f.close()
            f = open(path,"a")
            f.write(edited_text + "\n")
            f.close()
            print("edit saved!")
            return True
        else:
            print("Text file does not exist!:\n")
            return False
    def DeletingDescription(self,text,path):
        if os.path.isfile(path):
            f = open(path,"r")
            s= f.read()
            f.close()
            chngdtext=s.replace(text,"")
            f = open(path,"w")
            f.write(chngdtext)
            f.close()
            print("Done! Deleted the selected text successfully!")
            return True
        else:
            print("Text file does not exist!:\n")
            return False
    def ClearDatasetFile(self,path):
        if os.path.isfile(path):
            f = open(path,"w")
            f.write("")
            f.close()
            print("Done! cleared the selected dataset file successfully!")
            return True
        else:
            print("Text file does not exist!:\n")
            return False
        
        

        
