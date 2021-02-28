FROM python:rc-buster
COPY app /usr/share/app
WORKDIR /usr/share/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]