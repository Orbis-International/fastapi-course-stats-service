import pandas as pd
from datetime import datetime, timedelta

def process_top_5_courses(local_file_path):
    """
    Processes the CSV file to:
    - Remove unwanted course titles.
    - Filter by date and isActive.
    - Return the top 5 courses by counts.
    """
    # List of course titles to be removed
    courses_to_remove = [
        "Webinar", "webinar", "Ready for Take Off?", 
        "Module 1: Optic disc", "Module 2: Optic Neuropathy", 
        "Module 3: Pupil", "Module 4: Unexpected Vision Loss", 
        "Module 5: Ocular Motility", "Module 6: Systemic Conditions"
    ]
    
    try:
        # Load the CSV into a pandas DataFrame
        df = pd.read_csv(local_file_path)
        
        # Remove rows where CourseName contains any of the listed patterns
        course_name_pattern = '|'.join(courses_to_remove)
        df = df[~df['CourseName'].str.contains(course_name_pattern, case=False, na=False)]
        
        # Convert DateStarted column to datetime
        df['DateStarted'] = pd.to_datetime(df['DateStarted'], errors='coerce')

        # Filter out rows where DateStarted is older than 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        df = df[df['DateStarted'] >= thirty_days_ago]

        # Filter out rows where IsActive is True
        df = df[df['IsActive'] == False]

        # Get the top 5 courses and their counts
        top_5_courses = df['CourseName'].value_counts().head(5).to_dict()

        return top_5_courses

    except Exception as e:
        raise Exception(f"Error processing the data: {e}")
