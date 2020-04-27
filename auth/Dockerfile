FROM alpine:edge
RUN apk add --update py3-pip
RUN apk add gcc
RUN apk add python3-dev
RUN apk add --no-cache libressl-dev musl-dev libffi-dev

COPY requirements.txt /usr/src/auth/

RUN pip install --no-cache-dir -r /usr/src/auth/requirements.txt

RUN apk del libressl-dev musl-dev libffi-dev

COPY . /usr/src/auth/
EXPOSE 5000
CMD ["python3", "/usr/src/auth/auth.py"]
