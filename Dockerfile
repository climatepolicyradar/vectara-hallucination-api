# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Putting source code COPY last so we don't have to keep rebuilding the dependency install
# But need this for poetry install to work
COPY ./pyproject.toml /app/pyproject.toml

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Make port 5000 available to the world outside this container
EXPOSE 80


# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]