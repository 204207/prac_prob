FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /BestTrans_api
ADD requirements.txt /BestTrans_api/
RUN pip install -r requirements.txt
ADD . /BestTrans_api/