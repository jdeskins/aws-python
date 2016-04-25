# aws-python

Simple Docker container that providers workspace to run aws commandline tools in python.

## Examples

### Get AWS ECR login string for docker

You can run the helper script:

```
./samples/get-docker-login.sh
```

This script can be called from GoCD server after the build.sh script has built the new image.
It uses AWS environment variables to authenticate.  The container launches, runs the script,
then exists.

Or you can run the docker command directly:

```
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
    jdeskins/aws-python aws ecr get-login
```

### List Object Version Data from S3

```
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
    jdeskins/aws-python \
    list-versions.py -b bucket_name -p path_prefix
```

### List ECR Images using local credentials file

```
docker run --rm -v ~/.aws:/root/.aws jdeskins/aws-python aws ecr list-images \
    --repository-name=[REPOSITORY_NAME] \
    --profile=[PROFILE_NAME]
```

Uses AWS environment variables to authenticate and get version data of all objects in the bucket
matching the prefix

## Available Scripts

### Delete Untagged ECR Images

```
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION jdeskins/aws-python \
    ./scripts/cleanup-docker-images.py [REGISTRY_ID] [REPOSITORY_NAME]
```
