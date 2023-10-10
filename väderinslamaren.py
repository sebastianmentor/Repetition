import requests
import openpyxl
import os


def start_up_func():
    if not os.path.isfile('sample_file.xlsx'):
        # Create file
        ...

def run():
    while True:
        print('Meny -----')
        val = input('>>>')
        if val == '1':
            # 1. Hämta data från smhi
            # 2. Transformera data (dvs extrahera den data vi vill ha, 24 timmar)
            # 3. formatera så att det kan skrivas till excelfilen och lägg till ny prognos
            pass
        
        elif val == '2':
            # Läs in data från excelfil och sedan 
            # formatera för utrskrift
            pass

        elif val == '9':
            break
    #<--------------------END_OF_FUNCTION
if __name__ == '__main__':
    start_up_func()
    run()
    #<---------Kommer hit
#<--------Och avslutar