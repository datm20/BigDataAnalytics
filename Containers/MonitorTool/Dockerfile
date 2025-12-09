FROM python:3.11-slim
WORKDIR /app
COPY . .
VOLUME ./src:/app/src
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt


CMD ["flask", "--app", "src/index", "run", "-h", "0.0.0.0", "-p", "8080", "--debug"]
