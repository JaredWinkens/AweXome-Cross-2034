How to install AweXome Cross 2034 from base code

1. Have PyInstaller installed on your system(I recommend doing this in command prompt)
use this command to install it: pip install -U pyinstaller
2. cd into the folder that holds the main.py file
    ex. cd cs370, then cd AweXome-Cross-2034
3. Run python -m PyInstaller --onefile main.py
    This will create a dist folder if there is not one present and put the new executable file in it.
4. Then you can either move this file into the AweXome Cross 2034 folder and run it or make a copy of the assets folder and place it in the dist folder with the executable
5. Play test it 