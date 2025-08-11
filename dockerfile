# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /server

# Copy only the necessary files
COPY counter-service.py /server/

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port 80
EXPOSE 80

# Run the Flask app
CMD ["python", "counter-service.py"]
