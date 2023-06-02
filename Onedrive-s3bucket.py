import os
import boto3

# Get the S3 bucket name and the path to the OneDrive folder.
bucket_name = "onedrive-backup-bucket"
onedrive_folder_path = "/mnt/c/Users/qdaems/OneDrive - Guest-Tek Interactive Entertainment Ltd"

# Create a boto3 client for S3.
s3_client = boto3.client("s3")

# Upload the contents of the OneDrive folder to the S3 bucket.
for file in os.listdir(onedrive_folder_path):
    s3_client.upload_file(os.path.join(onedrive_folder_path, file), bucket_name, file)