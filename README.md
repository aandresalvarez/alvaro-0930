# alvaro-0930

##  Named Entity Recognition Service

Instructions:

* To start all services : 
```console
docker-compose up --build  
```
* To open the UI  and see the  H2o Wave Framework working go to : 
```url
http://localhost:10101/ner_ui 
```

* To test the functional API returning entities with  the spaCy model: 
```url
http://localhost:8080/docs
```
the code of the Fast-API service executing spaCy model is here: [main.py](/api/main.py)

### WHAT IS PENDING?

Finish the code for the file [ner_ui.py](ner_ui.py)


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


