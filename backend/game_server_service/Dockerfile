# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the service files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8001

# Command to start the FastAPI service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
