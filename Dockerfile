FROM python:3.10-slim
RUN pip install feedparser
COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["python", "/entrypoint.py"]
