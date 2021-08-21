from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
#import json
import spacy


## ++++++++ Spacy Model ++++++++++

nlp = spacy.load('en_core_web_sm')
def model_ner_spacy(sentence):
    arr=[]
    doc = nlp(sentence)
    for ent in doc.ents:
        yield ent.text, ent.label_


##++++++++++ API ++++++++++++++++

class Sentences_NER(BaseModel):
    text: str
    

app = FastAPI(title="spacy NER", description="Text label extraction NER")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}



@app.post("/ner")
async def read_sentence(sentence_obj: Sentences_NER):
    sentence=str(sentence_obj.text)
    if sentence and not sentence.isspace():
        #sentence = "Apple is looking at buying U.K. startup for $1 billion"
        results=list(model_ner_spacy(sentence))
    else:
         
        results="Error: This is the result if no input"
           
    return {"ner_result":results}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     # arr=[]
#     # nlp = spacy.load('en_core_web_sm')
#     # sentence = "Apple is looking at buying U.K. startup for $1 billion"
#     # doc = nlp(sentence)
#     # for ent in doc.ents:
         
#     return {"item_id": item_id, "q": arr}


        