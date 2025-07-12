# Autotrack Backend

A Dockerized Django backend to track and automate system tasks like:

- Scheduling daily/weekly tasks
- Sending alerts for failed runs
- REST APIs to view, create, update, delete tasks
- Built-in Django admin
- Containerized with Docker

## Run Locally

```bash
docker build -t autotrack-backend -f docker/Dockerfile .
docker run -p 8000:8000 autotrack-backend
