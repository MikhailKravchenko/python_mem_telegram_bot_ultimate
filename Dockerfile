FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 netcat nano vim htop nginx
RUN pip install --upgrade pip

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 443

COPY . /code/
#CMD ["tail", "-f", "/dev/null"]

CMD ["python", "/code/src/core.py"]
