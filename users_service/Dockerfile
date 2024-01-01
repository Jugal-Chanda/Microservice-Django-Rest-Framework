# Use an official Python runtime as a parent image
FROM python:3.9.18-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG app_port

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./.docker/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE ${app_port}

RUN pip install gunicorn==21.2.0

# Run management command for the notification service
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "users_service.wsgi"]
