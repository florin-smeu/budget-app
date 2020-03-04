FROM alpine:edge
RUN apk add --update py3-pip
COPY requirements.txt /usr/src/client/
RUN pip install --no-cache-dir -r /usr/src/client/requirements.txt
COPY client.py /usr/src/client/
COPY templates/index.html /usr/src/client/templates/
EXPOSE 5001
CMD ["python3", "/usr/src/client/client.py"]
