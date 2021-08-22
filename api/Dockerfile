FROM python:3.8-slim

# WORKDIR /usr/src/app
#ADD requirements.txt .
COPY ./api/requirements.txt requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update
RUN apt-get install -y build-essential python-dev git
RUN apt-get install gcc
RUN pip install --upgrade pip setuptools
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
 







