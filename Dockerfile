FROM python:3.11
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN  pip3 install -r requirements.txt
RUN mkdir templates
COPY app/* .
ENV GOOGLE_APPLICATION_CREDENTIALS=data-science.json
ENTRYPOINT [ "python" ]
CMD ["app.py" ]