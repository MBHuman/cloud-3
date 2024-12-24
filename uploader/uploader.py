import os
import boto3

def upload_file(bucket_name, file_name, client):
    client.upload_file(file_name, bucket_name, file_name)
    print(f"Uploaded: {file_name}")

if __name__ == "__main__":
    minio_endpoint = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
    access_key = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    secret_key = os.getenv("MINIO_SECRET_KEY", "minioadmin")

    s3 = boto3.client(
        's3',
        endpoint_url=minio_endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    bucket_name = "test-bucket"

    # Iterate and generate 13MB files, then upload
    for i in range(1, 101):
        file_name = f"file_{i}.txt"
        try:
            # Generate a 13 MB file with random data
            with open(file_name, "wb") as f:
                f.write(os.urandom(13 * 1024 * 1024))  # 13 MB

            # Upload the file to the bucket
            upload_file(bucket_name, file_name, s3)
        except Exception as e:
            print(f"Error uploading file {file_name}: {e}")
        finally:
            # Remove the local file after upload
            if os.path.exists(file_name):
                os.remove(file_name)
