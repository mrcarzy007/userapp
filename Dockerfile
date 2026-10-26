FROM python:3.13-slim as builder 
WORKDIR /app
COPY . . 
RUN pip install --user -r requirements.txt
FROM python:3.13-slim as production
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000
CMD ["python", "app.py"]
