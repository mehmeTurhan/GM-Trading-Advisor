FROM python:3.9.10-alpine3.14
WORKDIR /gainers
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install requests

COPY . .
ENV FLASK_APP=gainers
EXPOSE 8081

CMD ["python", "gainers.py"]