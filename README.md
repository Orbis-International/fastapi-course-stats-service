# FastAPI Course Stats Service

## Description

The **FastAPI Course Stats Service** is an API that retrieves and processes course data stored in AWS S3, designed to return the top 5 courses by user participation. This service uses FastAPI for high-performance API handling, along with pandas for data processing. The service is built to handle CSV data stored in an S3 bucket, allowing filtering and analysis of the data before presenting the top course stats.

### Features
- **S3 Integration**: Downloads CSV files from AWS S3 using boto3.
- **Data Processing**: Filters out irrelevant courses, removes inactive courses, and focuses on recent data (last 30 days).
- **Top 5 Courses**: Returns the top 5 most popular courses.
- **FastAPI**: A lightweight, high-performance API for fast data retrieval.
- **Dynamic Date Filtering**: Automatically filters courses that started more than 30 days ago.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [License](#license)

## Technologies

- **FastAPI**: A modern web framework for creating APIs with Python.
- **Pandas**: For data manipulation and processing.
- **Boto3**: AWS SDK for Python, used for S3 file handling.
- **Uvicorn**: ASGI server for running the FastAPI app.

## Installation

### Prerequisites
- **Python 3.8+**
- AWS credentials configured for S3 access
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed for setting up the AWS profile.

### Clone the repository:
```bash
git clone https://github.com/your-username/fastapi-course-stats-service.git
cd fastapi-course-stats-service
```

### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file or export the following environment variables in your shell:

```bash
BUCKET_NAME=your-s3-bucket-name
OBJECT_KEY=AbsorbPython/AbsorbPython.csv  # Modify as needed
LOCAL_FILE_PATH=AbsorbPython.csv
AWS_PROFILE=your-aws-profile  # Set your AWS CLI profile name
```

These variables can also be directly added to the `os.getenv` calls in the code if you prefer hardcoding them.

## Usage

### Running the App
Start the FastAPI server using `uvicorn`:

```bash
uvicorn app:app --reload
```

This will start the server locally at `http://127.0.0.1:8000`.

### API Endpoints

#### `GET /top-5-courses`

Returns the top 5 courses by user participation after processing data from the S3 bucket.

Example response:
```json
{
  "top_5_courses": {
    "Course 1": 120,
    "Course 2": 98,
    "Course 3": 75,
    "Course 4": 60,
    "Course 5": 50
  }
}
```

### Docker (Optional)
If you'd like to containerize the application, use the included `Dockerfile`.

#### Build the Docker image:
```bash
docker build -t fastapi-course-stats-service .
```

#### Run the Docker container:
```bash
docker run -d -p 8000:8000 --env-file .env fastapi-course-stats-service
```

This will run the service in a container and expose it on port 8000.
