# words_quiz
This is a simple words quiz web app to help you learn and practice spelling a words given its Chinese meaning.

# File Structure:

The code is written in Python & Flask:

  - ./words_web.py
  
      the main web app.
  
  - ./lists
  
      the folder to host source words list files in plain txt format with a .txt suffix. 
  
  - ./static
  
      the folder to host background images, stylesheets and some static test pages
  
  - ./ templates
  
      the folder to host flask templates for file lists page, presentation page and test pages
  
# Usage:
  
  - to start the server:
    
        python words_web.py
      
      the app is using Flask default configuration, and you can access the app by http://localhost:5000
    
  - words files was located at ./lsits folder. a wors list file consists multi-lines of wors with it's English and Chinese meaning.
  
        eg: banana 香蕉
    
  - flash cards are for you to learn about each word
  - spelling quiz is for you to practise each word' spelling
