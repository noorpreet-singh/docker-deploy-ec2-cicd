# Dockerized FastAPI Deployment on AWS EC2 with GitHub Actions CI/CD

A beginner-friendly DevOps project that demonstrates how to automate the deployment of a Dockerized FastAPI application to an AWS EC2 instance using GitHub Actions.

The goal of this project was to understand the complete deployment workflow instead of deploying the application manually every time a change is made.

---

## Project Overview

In this project:

- Developed a simple FastAPI application
- Containerized the application using Docker
- Hosted the application on an AWS EC2 instance
- Configured GitHub Actions for automatic deployment
- Used GitHub Secrets to securely store deployment credentials
- Connected GitHub Actions to EC2 using SSH

Whenever code is pushed to the `main` branch, GitHub Actions automatically deploys the latest version to the EC2 instance.

---

## Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
Build & Deploy
     │
     ▼
AWS EC2 Instance
     │
Docker Container
     │
     ▼
FastAPI Application
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | Web Framework |
| Docker | Containerization |
| AWS EC2 | Hosting |
| GitHub Actions | CI/CD |
| GitHub Secrets | Secure Credentials |
| SSH | Remote Deployment |

---

## Project Structure

```
.
├── app/
│   ├── main.py
│   └── templates/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── Dockerfile
├── requirements.txt
├── userdata.sh
└── README.md
```

---

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions workflow starts automatically.
3. Workflow connects to the EC2 instance using SSH.
4. Existing Docker container is stopped (if running).
5. New Docker image is built.
6. New container is started.
7. Updated application becomes available on the EC2 public IP.

---

## Features

- Dockerized FastAPI application
- Automatic deployment using GitHub Actions
- Secure deployment with GitHub Secrets
- Remote deployment through SSH
- Beginner-friendly project structure
- Easy to extend for future DevOps projects

---

## How to Run Locally

Clone the repository

```bash
git clone https://github.com/noorpreet-singh/docker-deploy-ec2-cicd.git
cd docker-deploy-ec2-cicd
```

Build Docker image

```bash
docker build -t fastapi-app .
```

Run Docker container

```bash
docker run -d -p 8000:8000 fastapi-app
```

Open your browser

```
http://localhost:8000
```

---

## GitHub Secrets Used

The following secrets are configured in GitHub Actions:

| Secret | Description |
|---------|-------------|
| EC2_HOST | Public IP of EC2 |
| EC2_USERNAME | SSH username |
| SSH_PRIVATE_KEY | Private key for EC2 login |

---

## Screenshots

### 1. GitHub Actions Successful Workflow

```
images/github-actions-success.png
```

**Screenshot should show:**

- Workflow completed successfully (green check)
- All deployment steps passed
- Repository name visible

---

### 2. Application Running on EC2

```
images/application-running.png
```

**Screenshot should show:**

- Browser opened with EC2 Public IP
- FastAPI application home page
- Simple response confirming deployment

---

## Challenges Faced

During this project I encountered several issues and learned how to troubleshoot them.

- SSH authentication errors
- Docker permission issues
- GitHub Secrets configuration
- EC2 Security Group configuration
- Docker container restart during deployment

These problems helped me better understand the deployment process instead of only following tutorials.

---

## What I Learned

- Docker basics and container lifecycle
- FastAPI deployment
- AWS EC2 instance management
- GitHub Actions workflow creation
- Secure deployment using GitHub Secrets
- Automating deployments using CI/CD

---

## Future Improvements

- Deploy using Application Load Balancer
- Store Docker images in Amazon ECR
- Use Terraform for infrastructure provisioning
- Configure HTTPS using ACM
- Add monitoring and logging

---

## Author

**Noorpreet Singh**

GitHub: https://github.com/noorpreet-singh

---

This project was built as part of my DevOps learning journey to gain hands-on experience with Docker, AWS, and CI/CD automation.
