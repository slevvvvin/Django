FROM python:3
RUN bash -c 'mkdir -p /code/{static}'
COPY . /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY entrypoint.sh /code
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
