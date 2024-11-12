# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Expose port for Flask
EXPOSE 5000

# Start Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
