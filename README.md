# Voting Poll Application

## Overview

This project is a Django web application for conducting voting polls. Users can create polls with multiple-choice questions, view details and results of existing polls, and vote on poll choices.


## Prerequisites

Before running the application, ensure that you have the following installed:

- Python (version 3.8)
- Docker


## Follow the instructions below:

 - Create a virtual environment:


    python -m venv .venv


    Activate the virtual environment:


    On Windows:
    venv\Scripts\activate

    On macOS and Linux:
    source .venv/bin/activate




- Install dependencies:
    pip install -r requirements.txt


    Run the application:
    python manage.py runserver



- Using Docker

    Clone the repository:
    git clone https://github.com/ChadleySnippers/L3T10---Capstone-Project---Consolidation.git

    cd your-repo


    Build the Docker image:
    docker build -t my-django-app .

    Run the Docker container:
    docker run -d -p 8000:8000 my-django-app
    Access the application in your web browser at http://localhost:8000.