FROM python:3
WORKDIR /devopsq4
COPY recvpod.py /devopsq4
COPY txpod.py /devopsq4
RUN pip install flask
RUN pip install requests
RUN pip install jsonify
CMD python recvpod.py
