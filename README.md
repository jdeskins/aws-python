# aws-python

Simple Docker container that providers workspace to run aws commandline tools in python.

## Examples

### Get AWS ECR login string for docker

```
./samples/get-docker-login.sh
```

This script can be called from GoCD server after the build.sh script has built the new image.
It uses AWS environment variables to authenticate.  The container launches, runs the script,
then exists.

### List Object Version Data from S3

```
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION jdeskins/aws-python \
    list-versions.py -b bucket_name -p path_prefix
```

Uses AWS environment variables to authenticate and get version data of all objects in the bucket
matching the prefix
