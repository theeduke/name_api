# REST API to manage person

The REST API is built using Flask framework and PostgreSQL for managing persons. It allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource.

## Table of Contents
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [UML Diagram](#database-modeling)  
- [Documentation](#documentation)  
- [Link to api](#link-to-api)  

## Prerequisites
Before getting started, ensure you have the following installed on your system:
- Python
- PostgreSQL (you can have it on local machine or have it hosted as a cloud service)

## Installation
Follow these steps to set up and run the project:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/theeduke/name_api.git
   ```

2. Run the following command to set up your virtual environment:
   ```bash
   python -m venv env
   ```
   ```bash
   env/Scripts/activate
   ```
   
4. Run the following to install dependencies:
   ```bash
   pip install Flask
   ```
   ```bash
   pip install psycopg2-binary
   ```
   ```bash
   pip install python-dotenv
5. Create a .env file in the project root and configure your postgreSQL database connection:
   ```bash
   DATABASE_URL=postgresql://username:password@localhost:5432/your_database
   ```
6. Use the following command to run server:
   ```bash
   python app.py
   ```
Your Flask server should now be running at http://localhost:5000.

## Database Modeling 
This UML diagram below represents the structure and relationships of the API's classes and models.

![uml diagram]('Untitled Workspace.png')


## Documentation 
 Here is the [postman](https://elements.getpostman.com/redirect?entityId=29720606-0ea67638-bda4-4b79-b7f2-533fac6c3c59&entityType=collection) documentation for the API 

## Link to API 
 The documentation include test to verify the API's fun
 ```bash
 https://name-api-nm40.onrender.com
 ```
