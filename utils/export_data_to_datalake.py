from minio import Minio
from minio.error import S3Error
from helpers import load_cfg
import os

CFG_FILE = './utils/cfg.yml'

def main():
    cfg = load_cfg(CFG_FILE)
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        cfg["datalake"]["endpoint"],
        access_key=cfg["datalake"]["access_key"],
        secret_key=cfg["datalake"]["secret_key"],
        secure=False,
    )

    # Create bucket if not exist.
    found = client.bucket_exists(cfg["datalake"]["bucket_name"])
    if not found:
        client.make_bucket(cfg["datalake"]["bucket_name"])
    else:
        print(f'Bucket {cfg["datalake"]["bucket_name"]} already exists')

    # Upload file.
    client.fput_object(
        cfg["datalake"]["bucket_name"], os.path.basename(cfg["fake_data_path"]), cfg["fake_data_path"],
    )

if __name__ == '__main__':
    main()