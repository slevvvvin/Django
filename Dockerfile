FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/static
COPY . /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY gunicorn.sh /code
COPY entrypoint.sh /code
RUN chmod +x /code/entrypoint.sh
RUN chmod +x /code/gunicorn.sh
ENTRYPOINT ["/code/entrypoint.sh"]