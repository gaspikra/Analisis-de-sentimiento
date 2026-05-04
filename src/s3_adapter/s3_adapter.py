import boto3
import os
import logging
logger  = logging.getLogger(__name__)
class S3Adapter:
    def __init__(self):
        self.endpoint_url = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")
        self.s3_client = boto3.client(
            "s3", 
            endpoint_url=self.endpoint_url,
            aws_access_key_id="test", 
            aws_secret_access_key="test"
        )

    def upload_file(self, local_path, bucket, s3_path):
        try:
            self.s3_client.upload_file(local_path,bucket,s3_path)
            logger.info(f"se subio el archivo {local_path} correctamente a s3://{bucket}/{s3_path}")
        except Exception as e:
            logger.exception(f"error al subir a S3: {e}")


    def download_file(self, bucket, s3_path, local_path):
        try:
            self.s3_client.download_file(bucket, s3_path, local_path)
            logger.info("Los datos se descargarron correctamente")
        except Exception as e:
            logger.exception(f"error al descargar datos")









