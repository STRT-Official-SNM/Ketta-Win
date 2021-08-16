import os
import time

def main():
    if os.path.exists("installationRegistrary") == False:

        print("This script may require sudo permissions...")

        print("[*] downloading required python modules...")
        os.system("pip install webrtcvad selenium")
        os.system("pip install SpeechRecognition pyaudio")
        
        time.sleep(3)

        print("Finishing script")
        f= open("installationRegistrary","w+")
        f.close()

    else:
        if os.path.exists("installationRegistrary") == True:
            print("Hey user, a registrary has been registered. If you think there is a mistake, you can delete the installationRegistrary file")

            
main()
