FROM python

WORKDIR /Docker-first-app

COPY requirements.txt .

COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python","./src/main.py"]