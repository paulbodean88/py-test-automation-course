FROM python:3.8.2

RUN apt update && apt install -y gdebi-core libnss3 libgconf-2-4

ADD google-chrome-stable_current_amd64.deb .
RUN gdebi -n google-chrome-stable_current_amd64.deb

WORKDIR /t4_ui_testing
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD chromedriver .
RUN chmod +x chromedriver
ADD selenium_test.py .

CMD python selenium_test.py