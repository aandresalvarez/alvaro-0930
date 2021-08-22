# Import `Site` and the `ui` module from the `h2o_wave` package
from h2o_wave import site, ui,main
import time
import requests

def mifun(text):
    if len(text)<1:
        return text
    else:
        response = requests.post('http://api/ner', data = {'text':'Each component, API-Service'})
        #print(response)
        return response
# Get the web page at route '/demo'.
# If you're running this example on your local machine,
# this page will refer to http://localhost:10101/demo.
page = site['/ner_ui']

# Add a Markdown card named `hello` to the page.
# page['hello'] = ui.markdown_card(
#     box='1 1 2 2',
#     title='Hello World!',
#     content='And now for something completely different!',
# )
text='asdf'
page['ner'] = ui.form_card(box='1 1 4 10', items=[
        ui.textbox(name='text', label='English', value=text or '', multiline=True),
        ui.label('Pig Latin'),
        ui.text(mifun(text) or '*Type in some text above to translate to Pig Latin!*'),
    ])

beer_verse = '''={{before}} bottles of beer on the wall, {{before}} bottles of beer.

Take one down, pass it around, {{after}} bottles of beer on the wall...
'''

beer_card = page.add('wall', ui.markdown_card(
    box='6 1 4 2',
    title='99 Bottles of Beer',
    content=beer_verse,
    data=dict(before='99', after='98'),
))



for i in range(99, 0, -1):
    beer_card.data.before = str(i)
    beer_card.data.after = str(i - 1)
    page.save()
    time.sleep(1)


 




