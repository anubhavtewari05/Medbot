# Medbot
🏥 Build a Complete Medical Chatbot with LLMs, LangChain, Pinecone, Flask & AWS

This project demonstrates how to build and deploy a Medical Chatbot using LangChain, Pinecone, Groq, Flask, and AWS (ECR + EC2 + GitHub Actions CI/CD).
The chatbot leverages RAG (Retrieval-Augmented Generation) with Pinecone vector storage for medical knowledge and Groq LLMs for fast, reliable responses.




⚙️ Tech Stack

Python 3.10+

LangChain – Orchestration of LLM workflows

Flask – Web framework for chatbot API/frontend

Groq LLMs – For fast and efficient inference

Pinecone – Vector database for embeddings

Docker – Containerization

AWS EC2 & ECR – Deployment infrastructure

GitHub Actions – CI/CD automation





🚀 Getting Started (Local Setup)
1. Clone the Repository
git clone <repo_name>

2. Create a Conda Environment
conda create -n medibot python=3.10 -y
conda activate medibot

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the root directory:

PINECONE_API_KEY = "your-pinecone-api-key"
GROQ_API_KEY = "your-groq-api-key"

5. Store Embeddings to Pinecone
python store_index.py

6. Run the Application
python app.py


Now open: http://localhost:8080




☁️ AWS Deployment Guide
1. Login to AWS Console

Create an IAM User with following permissions:

AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

2. Create an ECR Repository

Example repo URI:

315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

3. Launch EC2 Instance (Ubuntu)

Install Docker inside EC2:

sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

4. Configure GitHub Actions Runner

Go to Settings > Actions > Runners > New self-hosted runner

Follow instructions for Ubuntu

5. Add GitHub Secrets

In GitHub repo → Settings > Secrets and variables > Actions → Add:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
GROQ_API_KEY

6. CI/CD Flow

GitHub Actions builds Docker image

Pushes image → AWS ECR

EC2 pulls image

Runs containerized chatbot

📜 Project Workflow

User Query → Flask Frontend

LangChain → Retrieve relevant context from Pinecone

Groq LLM → Generate response based on context

Flask → Serve response to user

📌 Future Improvements

Add authentication for secure chatbot usage

Multi-modal input support (text + medical images)

Monitoring and logging with AWS CloudWatch
