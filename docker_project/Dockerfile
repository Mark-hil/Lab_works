
FROM nginx:1.10.1-alpine

# Set the working directory inside the container
WORKDIR /myapp

# Copy all files in the current directory to the /app directory in the container
COPY template/html /usr/share/nginx/html

# Install Flask inside the container
RUN pip install flask

# Expose port 5000 (the port Flask is running on)
EXPOSE 5000

# Command to start the Flask app
CMD ["python", "myapp.py"]
