FROM python:3.8.6-buster
WORKDIR /app

# Install packages
RUN apt update -y
RUN apt install tmux -y
RUN apt install vim -y

# Install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code
RUN mkdir /app/src
COPY /src src/
RUN cd src

# Run application
EXPOSE 5000
CMD sh -c "python src/server/server_run.py"

