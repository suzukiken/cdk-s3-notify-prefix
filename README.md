
python -m venv test/env
source test/env/bin/activate
python -m pip install boto3

export BUCKET_NAME=
python test/put_s3.py