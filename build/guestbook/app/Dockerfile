FROM python:rc-buster
COPY app /usr/share/app
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR app
CMD [ "python3", "app.py"]