FROM python:rc-slim-buster

WORKDIR /usr/src/app

COPY module_PRJ.py .
COPY user_manager.py .
COPY admin_manager.py .

RUN pip install pymysql

ENTRYPOINT [ "python"]
CMD [ "./module_PRJ.py" ]
