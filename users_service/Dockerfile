# Use an official Python runtime as a parent image
FROM python:3.9.18-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django application for the user service
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]