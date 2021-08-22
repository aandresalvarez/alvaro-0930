"""

WORK IN PROGRESS

TO DO LIST:

    - Fix the API request in the function Call_NER_Api(sentence) 
        Current error:
        Max retries exceeded with url: /ner/ (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f9a292cecd0>: Failed to establish a new connection: [Errno 111] Connection refused')  
        

    - Implement this page vie "wave run"  instead of a static page
      Example : https://wave.h2o.ai/docs/tutorial-counter


    -   Assembble API Call and UI to return Entities       


RUN:

If you're running this file on your local machine,
this page will refer to http://localhost:10101/ner_ui.

"""


from h2o_wave import site, ui,main
import requests



#++++++++++++++++++API CALL++++++++++++

url = "http://api:8000/ner"
def Call_NER_Api(sentence):
    payload = "{\"text\": \"The cat is the great animal in the house\"}"
    headers = {
    'Content-Type': 'application/json'
    }

    if sentence and not sentence.isspace():
        response = requests.request("POST", url, headers=headers, data = payload)
        return response.text.encode('utf8')
    else:
        return "Error"


#++++++++++++++++++H2O WAVE UI++++++++++++

page = site['/ner_ui']

text=''
page['ner'] = ui.form_card(box='3 2 7 6', items=[
        ui.textbox(name='text', label='Named Entity Recognition, please type in some text', value=text or '', multiline=True),
        ui.label(' Results of the  Named Entity Recognition Model:'),
        ui.text("CallApi(text)" or '*Type in some text above to Run Named Entity Recognition Model!!'),
    ])
page.save()

 




