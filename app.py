from fastapi import FastAPI, HTTPException
from s3_utils import download_file_from_s3
from data_processing import process_top_5_courses
import os
from dotenv import load_dotenv


app = FastAPI()

# Define S3 bucket and file info (these should be stored in environment variables or a config file)
BUCKET_NAME = os.getenv('BUCKET_NAME')
OBJECT_KEY = os.getenv('OBJECT_KEY')
LOCAL_FILE_PATH = os.getenv('LOCAL_FILE_PATH')
AWS_PROFILE = os.getenv('AWS_PROFILE')

# # AWS credentials (should be set as environment variables for security)
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN', None)  # Optional session token


@app.get("/top-5-courses")
async def get_top_5_courses():
    """
    Endpoint to get the top 5 courses by their counts.
    - Downloads the CSV from S3.
    - Processes the DataFrame to filter out irrelevant data.
    - Returns the top 5 courses by counts.
    """
    try:
        # Step 1: Download the file from S3
        download_file_from_s3(BUCKET_NAME, OBJECT_KEY, LOCAL_FILE_PATH, AWS_PROFILE)
        # download_file_from_s3(BUCKET_NAME, OBJECT_KEY, LOCAL_FILE_PATH, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN)

        # Step 2: Process the file and get the top 5 courses
        top_5_courses = process_top_5_courses(LOCAL_FILE_PATH)
        
        # Return the result as a JSON response
        return {"top_5_courses": top_5_courses}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
