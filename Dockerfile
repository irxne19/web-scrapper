FROM python:3.10.1
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["bash"]