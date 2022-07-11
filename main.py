import tkinter as tk
from tkinter.font import Font
import pyperclip as pc
import json

try:
    with open('htfconfig.json','r') as f:
        f.read()
except:
    with open('htfconfig.json', 'a+') as f:
                f.write('{"use":false}')


config = json.loads(open('htfconfig.json').read())
use = config['use']

class App:
    def __init__(self, root):
        self.use = use
        #setting title
        root.title("HFT")
        #setting window size
        width=200
        height=105
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Checkbox=tk.Checkbutton(root)
        Checkbox["justify"] = "center"
        Checkbox["text"] = """Use ' ' instead of " " """
        Checkbox.place(x=10,y=30,width=180, height=10)
        Checkbox["offvalue"] = "0"
        Checkbox["onvalue"] = "1"
        Checkbox["command"] = self.change
        if self.use == True: Checkbox.select()

        Button=tk.Button(root)
        Button["justify"] = "center"
        Button['text'] = 'Format'
        Button.place(x=10,y=45,width=180,height=45)
        Button["command"] = self.form

        font = Font(root=root,font=None,size=8)

        self.Label=tk.Label(root)
        self.Label["justify"] = "center"
        self.Label["text"] = "Hello World"
        self.Label['font'] = 18
        self.Label.place(x=10,y=5,width=180,height=15)

        Label1=tk.Label(root)
        Label1["justify"] = "center"
        Label1["text"] = "github.com/pyrgasm"
        Label1['font'] = font
        Label1.place(x=25,y=90,width=150,height=13)

    def form(self):
        # Format
        try:
            symbol = "'" if self.use==True else '"'

            headers = pc.paste().splitlines()
            result = 'headers = {\n'

            for header in headers:
                result += f"""    {symbol}{header.split(': ')[0]}{symbol}: {symbol}{header.split(': ')[1]}{symbol},\n"""

            result += '}'
            pc.copy(result)
            print(result)
            self.Label["text"] = "Done"
        except Exception as e:
            self.Label["text"] = "Error"
        
    def change(self):
        self.use = True if self.use == False else False
        print(self.use)
        with open('htfconfig.json', 'w') as f:
            if self.use == False:
                json.dump({'use':False}, f)
            else:
                json.dump({'use':True}, f)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()