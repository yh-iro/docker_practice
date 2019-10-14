FROM python
RUN pip install flask
RUN pip install psycopg2
ADD hello.py /home/
ENTRYPOINT ["python", "/home/hello.py"]
