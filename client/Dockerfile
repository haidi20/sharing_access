FROM python:3.9

RUN apt-get update && apt-get install -y \
  && apt-get install -y iputils-ping \
  python3-pip

RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# COPY . .