FROM python:3.11-slim

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Java and other dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install poetry && poetry install

## Default command
#CMD ["python", "apollo/main.py", "--layer", "bronze", "--table", "customer", "--load_type", "inc"]

