FROM mcr.microsoft.com/devcontainers/base:ubuntu
RUN apt update && apt upgrade \
    && apt install -y git python3-full python3-pip vim
RUN curl -fsSL https://ollama.com/install.sh | sh