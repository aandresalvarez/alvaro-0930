FROM python:3.7
COPY ./ui/python/requirements.txt requirements.txt
RUN pip --default-timeout=100 install -r requirements.txt
CMD ["python","ner_ui.py"]
#RUN cd $HOME/wave-apps
#RUN source venv/bin/activate
#RUN wave run ner_ui