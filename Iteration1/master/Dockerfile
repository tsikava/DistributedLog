# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY master.py master.py

# Expose the HTTP port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "master:app", "--host", "0.0.0.0", "--port", "8000"]
