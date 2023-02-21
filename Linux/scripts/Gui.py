from tkinter import *
import validators
import Parser
import subprocess

root = Tk()
root.geometry("300x300")
root.title("HAPTICOM URL PARSER")
 
def take_input():
    INPUT = InputText.get("1.0", "end-1c")
    # print(INPUT)
    if(validators.url(INPUT)):
        create_directory()
        Parser.parser(INPUT)
        Output.delete("1.0","end-1c")          
        Output.insert('end', 'The website was parsed, use button to open file') 
        HyperLink.pack()             
    else:
        Output.insert(END, "URL is not valid")

def open_file():
    link = f"../Parsed_Files/{Parser.filename}.txt"
    result = subprocess.run(['xdg-open', f'{link}'], stdout=subprocess.PIPE)

def create_directory():
    subprocess.run(['mkdir','-p', '../Parsed_Files'], stdout=subprocess.PIPE)    
   

l = Label(text = "Paste URL for Parsing")
InputText = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
 

# r = Take_input()
HyperLink = Button(root, text='Open File', command = lambda:open_file())

Output = Text(root, height = 5,
              width = 25,
              bg = "light cyan")

Display = Button(root, height = 2,
                 width = 20,
                 text ="Parse",
                 command = lambda:take_input())
l.pack()
InputText.pack()
Display.pack()
Output.pack()                

# 
mainloop()