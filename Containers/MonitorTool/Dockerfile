FROM python:3.11-slim
WORKDIR /app
COPY . .
VOLUME ./src:/app/src
EXPOSE 9090
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/sh", "-c", "python3 src/monitor.py & exec flask --app src/index run -h 0.0.0.0 -p 9090 --debug"]
