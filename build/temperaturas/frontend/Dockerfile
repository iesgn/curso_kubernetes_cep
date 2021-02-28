FROM python:rc-buster
COPY app /usr/share/app
WORKDIR /usr/share/app
RUN pip install --no-cache-dir -r requirements.txt
ENV TEMP_SERVER temperaturas-backend:5000
EXPOSE 3000
CMD [ "python3", "app.py"]
