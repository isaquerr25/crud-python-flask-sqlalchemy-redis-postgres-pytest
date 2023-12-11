# Docker Compose

This is a step-by-step guide to running an application using Docker Compose. Make sure you have Docker and Docker Compose installed on your machine before getting started.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/): Installation of Docker
- [Docker Compose](https://docs.docker.com/compose/install/): Installation of Docker Compose

## How to Use

Execute Docker Compose to build and start the containers:

```bash {"id":"01HHB8KWFKDEHNCWVH7CVZ4V0B"}
docker-compose up -d
```

This will start the containers in the background. If you prefer to view real-time logs, omit the `-d` option.

5. Wait until all services are completely started.

6. Access the application in your browser using the appropriate URL. The default is http://localhost:PORT, where PORT is the port defined in the `.env` file.

## Useful Docker Compose Commands

- Start the containers:

```bash {"id":"01HHB8KWFKDEHNCWVH7F9HTMMT"}
docker-compose up -d
```

Make sure to adjust this guide as needed to meet the specific requirements of your project.

# Python Installation

## Download and Install Python:

1. Download the latest version of Python from [python.org](https://www.python.org/).
2. Run the installer and check the option "Add Python to PATH" during the installation.

## Create a Virtual Environment (venv)

### Open Terminal (Linux/Mac) or PowerShell (Windows):

1. Open the terminal or PowerShell on your operating system.

2. Navigate to the Project Directory:

   Use the `cd` command to navigate to the directory where you cloned or created your project.

3. Create a Virtual Environment:

Run the following command to create a virtual environment:

```bash {"id":"01HHB8KWFMF2ZH91YM7M53CPFA"}
python -m venv venv
```

Activate Virtual Environment:

Activate the virtual environment. The procedure may vary depending on the operating system:

On Windows (PowerShell):

```sh
.\venv\Scripts\Activate
```

On Linux/Mac:

```sh
source venv/bin/activate
```

Installation of Dependencies
Install Project Dependencies:
With the virtual environment activated, use the following command to install project dependencies:

```sh
pip install -r requirements.txt
```

Running Tests with Pytest
Execute Tests:
With the dependencies installed, run the Pytest command:

```sh
python test_app.py
```

This will execute all tests in the project.





