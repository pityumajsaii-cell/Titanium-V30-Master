FROM ubuntu:22.04
RUN apt-get update && apt-get install -y bash curl python3
COPY . /app
WORKDIR /app
chmod +x master_controller.sh
CMD ["./master_controller.sh"]
