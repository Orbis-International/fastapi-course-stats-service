import boto3
import os

def download_file_from_s3(bucket_name, object_key, local_file_path, aws_profile):
    """
    Download the file from S3 using the provided AWS profile.
    """
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.client('s3')

    try:
        s3.download_file(bucket_name, object_key, local_file_path)
        print(f"File {local_file_path} downloaded successfully!")
    except Exception as e:
        raise Exception(f"Error downloading file from S3: {e}")


# def download_file_from_s3(bucket_name, object_key, local_file_path, aws_access_key_id, aws_secret_access_key, aws_session_token=None):
#     """
#     Download the file from S3 using AWS access keys instead of profiles.
#     """
#     # Create an S3 client using the provided access keys
#     session = boto3.Session(
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         aws_session_token=aws_session_token  # Optional, use if needed for temporary credentials
#     )
#     s3 = session.client('s3')

#     try:
#         s3.download_file(bucket_name, object_key, local_file_path)
#         print(f"File {local_file_path} downloaded successfully!")
#     except Exception as e:
#         raise Exception(f"Error downloading file from S3: {e}")