import pyautogui as gui

def notFound(arg):
    gui.alert(f"The Command {arg} was not found. Type Help to see all commands")

def main():
    options = ["Submit"]
    command = gui.prompt(text = "Enter Command", title = "Max")

    # If Command Is Empty
    if command == "":
        gui.alert(text = "Command cant be Empty")
        command = gui.prompt(text = "Enter Command", title = "Commands")

    # print(command)
    return(command)

def search():
    query = gui.prompt(text = "Search Google", title = "Google Search")
    # print(query)
    return(query)

def downloadYT():
    url = gui.prompt(text = "Enter Video Url", title = "Enter URL")
    # print(url)
    return(url) 

def options():
    option = gui.confirm(text="Options", buttons = ["Only Audio", "Audio + Video"])
    return option

def projectName():
    file_name = gui.prompt(text = "Enter Project Name", title = "Enter Project name")
    return file_name

def projectType():
    projType = gui.confirm(text = "Project Type", buttons = ["Python", "NodeJS"])
    print(projType)
    return projectType
