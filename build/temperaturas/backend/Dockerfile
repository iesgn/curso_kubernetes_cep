FROM debian
RUN apt-get update && apt-get install -y python3-pip python3-lxml && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY app /usr/share/app
WORKDIR /usr/share/app
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]