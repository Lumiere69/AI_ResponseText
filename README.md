# AI_ResponseText
This program is designed to recognize text from an image and search for it on the Internet.


# Installation instructions on Linux:
1. You need to install tesseract, to do this, enter in the terminal "sudo apt-get install tesseract-ocr"
2. To install the language packs, enter "sudo apt-get install tesseract-ocr-eng", write the desired language instead of eng (English), the table of abbreviations - "https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html "
3. Download the AI_ResponseText archive and unpack
4. Find out the version of Google Chrome by the link "chrome://settings/help"
5. And download the desired version on Linux on the website "https://chromedriver.storage.googleapis.com/index.html "
6. Transfer to the AI_ResponseText folder
7. If venv is not installed, enter in the terminal "sudo apt install -y python3-venv"
8. Open AI_ResponseText enter in the terminal "python -m venv venv", "source venv/bin/activate", "pip install -r requirements.txt "
9. In the file search.py replace in 7, 23, 39, 55, 71 lines of the path with chromedriver
10. DONE!!! To run, we write the command "python3 main.py " in the terminal (instructions for use next).

# Installation instructions on Windows:
1. You need to install tesseract by following the link "https://github.com/UB-Mannheim/tesseract/wiki"
2. To install the language packs, download the file with the desired language from the link "https://github.com/tesseract-ocr/tessdata " and move it to the folder "C:\Program Files\Tesseract-OCR\tessdata" (if you have not changed the installation path), the table of abbreviations - "https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html "
3. Download the AI_ResponseText archive and unpack
4. Find out the version of Google Chrome by the link "chrome://settings/help"
5. And download the desired version on Windows on the website "https://chromedriver.storage.googleapis.com/index.html "
6. Transfer to the AI_ResponseText folder
7. In the read file.py in the 8th (empty) line, enter "pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' "
8. Open AI_ResponseText enter in the cmd "python -m venv venv", "venv\Scripts\activate.bat", "pip install -r requirements.txt "
9. In the file search.py replace in 7, 23, 39, 55, 71 lines of the path with chromedriver
10. DONE!!! To run, we write the command "python main.py " in the cmd (instructions for use next).

#Instructions for use:
1. To turn on/off the parser, you need to register "ep"/"dp" (by default, the parser is enabled).
2. To select a photo on which to recognize the text, you need to register the command "file= image.jpeg" (image.jpeg can be replaced with the name of your picture).
3. In the window that opens, select the text that needs to be recognized. (Left mouse button - selection, right mouse button - deselection). Closing the window. 
4. A ready-made file is issued with the selected text and the recognized words written above them. The entire text will be displayed in the console.
5. If you have not turned off the parser, it will open each line of text in 5 different search engines and save screenshots to the screen folder (it must be created).
