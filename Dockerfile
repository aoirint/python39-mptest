FROM python:3.9.0

WORKDIR /work
ADD main.py /work/

CMD [ "python3", "main.py" ]
