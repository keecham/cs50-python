def main():
    playback()

def playback():
   userinput = input("Say a few words: ")
   print (userinput.replace(" ", "..."))

main()