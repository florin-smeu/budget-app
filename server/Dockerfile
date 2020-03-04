FROM alpine:edge
RUN apk add --update py3-pip
COPY requirements.txt /usr/src/server/
RUN pip install --no-cache-dir -r /usr/src/server/requirements.txt
COPY server.py /usr/src/server/
COPY templates/index.html /usr/src/server/templates/
EXPOSE 5000
CMD ["python3", "/usr/src/server/server.py"]
