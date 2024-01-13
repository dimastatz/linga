FROM python:3.11-slim-buster

# Combine multiple apt-get to reduce docker layres
RUN apt-get update && apt-get install -y \
    ffmpeg \
    tesseract-ocr-all \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
    
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

RUN black linga tests
RUN pylint --fail-under=9.9 linga tests
RUN pytest --cov-fail-under=95 --cov linga -v tests

ENTRYPOINT ["python3"]
CMD ["./linga/app.py" ]