# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /myapp

# Copy the requirements.txt file to the working directory
COPY requirements.txt /myapp/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /myapp/

# Expose port 8000 (Django default port)
EXPOSE 8000

# Set the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
