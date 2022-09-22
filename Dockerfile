FROM python:3.8
WORKDIR /usr/app/src
RUN apt-get update && apt-get install -y \
    ffmpeg
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "-u", "./main.py"]