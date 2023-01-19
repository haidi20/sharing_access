FROM python:3.9
RUN apt-get update && apt-get install -y \
  python3-pip

RUN apt-get install -y gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev

RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .