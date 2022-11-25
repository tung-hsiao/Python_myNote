FROM ubuntu:20.04
LABEL INSTANCE_TYPE="myContainer"

## 設定系統語系 UTF-8
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y locales && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

## 安裝 Python
RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONIOENCODING utf-8
ENV PYTHONUNBUFFERED=1

## 設定系統 時區 Asia/Taipei
ENV TZ="Asia/Taipei"
ENV DEBIAN_FRONTEND noninteractive

## 爲了開發方便 安裝 curl, vim
RUN apt-get update && \
    apt-get -y install tzdata curl vim && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

## Change TimeZone
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

## 程式需要的 參數設定
### 資料庫連綫資訊
ENV VARIABLE_A="AAA"
ENV URL_B="BBBBB"


## 建立資料夾
# RUN mkdir -p /var/myLog/

## Set work directory
WORKDIR /opt/

## install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

## port
EXPOSE 5000

# CMD python main.py
# CMD tail -f /dev/null



