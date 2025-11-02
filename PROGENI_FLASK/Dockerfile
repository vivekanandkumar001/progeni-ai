# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Hugging Face port
EXPOSE 7860

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=7860

# Run Flask app
CMD ["python", "app.py"]
