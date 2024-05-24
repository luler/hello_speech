FROM python:3.7

MAINTAINER 1207032539@qq.com

RUN apt update -y && apt install -y libsndfile1

RUN pip install paddlepaddle==2.3.0 paddlespeech==1.0.1 -i https://mirror.baidu.com/pypi/simple

COPY . /root/work

WORKDIR /root/work

RUN pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple

EXPOSE 5000

ENV PPSPEECH_HOME /root/work/paddlespeech

CMD ["python","app.py"]