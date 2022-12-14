FROM python:latest

WORKDIR /myapp

COPY . .

#ENTRYPOINT ["./spamer.py", "-addr $IP_ADDR", "--port $TCP_PORT"]
CMD ["python3", "--IP_ADDR $IP_ADDR", "--port $TCP_PORT"]
