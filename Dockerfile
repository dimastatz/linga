FROM python:3.11-slim-buster

# Combine multiple apt-get to reduce docker layres
RUN apt-get update && apt-get install -y ffmpeg 