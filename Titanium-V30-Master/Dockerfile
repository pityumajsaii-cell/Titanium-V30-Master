FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git curl
RUN pip install --no-cache-dir flask requests bhast gunicorn
COPY . .
EXPOSE 7860
CMD ["python3", "app.py"]
