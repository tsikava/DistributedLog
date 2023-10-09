# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY secondary.py secondary.py

# Expose the HTTP port
EXPOSE 8001

# Start the FastAPI application
CMD ["uvicorn", "secondary:app", "--host", "0.0.0.0", "--port", "8001"]
