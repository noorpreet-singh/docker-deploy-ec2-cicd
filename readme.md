# Dockerized To-Do API with CI/CD on AWS EC2

This is my first project. I built a simple To-Do REST API using Python Flask, containerized it with Docker, and deployed it on an AWS EC2 instance. I also set up a basic CI/CD pipeline with GitHub Actions so that every push to `main` automatically deploys the latest code to the server.

## What I Built

- A small Flask API with in-memory todo storage (no database, kept it simple for this project)
- A Dockerfile to containerize the app
- docker-compose to build and run the container
- A GitHub Actions workflow that connects to EC2 over SSH and redeploys the app on every push

## Tech Used

- Python (Flask)
- Docker & Docker Compose
- AWS EC2
- GitHub Actions

## API Endpoints

| Method | Route     | What it does                  |
|--------|-----------|--------------------------------|
| GET    | /         | Returns a welcome message      |
| GET    | /todos    | Returns the list of todos      |
| GET    | /health   | Health check for the app       |

## How the Deployment Works

1. I push code to the `main` branch
2. GitHub Actions workflow runs automatically
3. It connects to my EC2 instance over SSH
4. On the server it pulls the latest code and runs `docker compose up -d --build`
5. Updated app goes live, no manual steps needed

## How to Run Locally

```
git clone https://github.com/noorpreet-singh/docker-deploy-ec2-cicd.git
cd docker-deploy-ec2-cicd
docker compose up --build
```

App runs at `http://localhost:5000`

## Screenshots

![API response](screenshots/todos-response.png)
*Screenshot should show the `/todos` endpoint response (JSON list of todos), taken from browser or Postman.*

![CI/CD pipeline run](screenshots/github-actions-run.png)
*Screenshot should show a successful run of the deploy workflow on the Actions tab of the repo.*

## What I Learned

This was my first time setting up an EC2 server, writing a Dockerfile from scratch, and connecting GitHub Actions to auto-deploy on push. It helped me understand how a CI/CD pipeline actually works end to end, not just in theory.
