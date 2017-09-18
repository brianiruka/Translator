"""
Example application showing the use of the Translate method in the Text Translation API.
"""

from xml.etree import ElementTree
from auth import AzureAuthClient
import requests

client_secret = '04f3074133324043b98a474374ca9ec9'
auth_client = AzureAuthClient(client_secret)
bearer_token = 'Bearer ' + auth_client.get_access_token()

from Tkinter import *


root = Tk()
root.wm_title("Translator")
root.minsize(width=300, height=300)
root.maxsize(width=600, height=300)



tb1 = Text(root,bg = '#fffaf2', height=10, width=40)
tb1.insert('1.0', 'Type in me...')

tb1.pack(pady=(20,0))

def select():
        sf = "English to %s" % var.get()
        root.title(sf)       
        input = tb1.get("1.0",END)

        if (var.get() == "Spanish"):
            lang = 'es'
        elif (var.get() == "German"):
            lang = 'de'
        elif (var.get() == "French"):
            lang = 'fr'
        else:
            lang = 'none'

        # Call to Microsoft Translator Service
        headers = {"Authorization ": bearer_token}
        translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(input, lang)
        translationData = requests.get(translateUrl, headers = headers)
        # parse xml return values
        translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
        tb1.delete(1.0, END)
        if (lang == 'none'):
                tb1.insert(INSERT, 'Please select a language to continue...')
        else:
                tb1.insert(INSERT, translation.text)
        

# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("Translator                ")
var = StringVar(root)
# initial value
var.set('Select A Language')
choices = ['Spanish', 'French', 'German']
option = OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)
button = Button(root, text="Translate", command=select)
button.pack(side='left', padx=20, pady=10)



root.mainloop()





        

