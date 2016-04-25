# aws-python

Simple Docker container that providers workspace to run aws commandline tools in python.


## Available Scripts

### Delete Untagged ECR Images

When image is tagged as "latest", the previously "latest" tagged version still exists but
is no longer tagged.  That container is cached for possible later re-use.
This script will remove all untagged containers from the repo for a given
REGISTRY_ID and REPOSITORY_NAME (image name).

```
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
    jdeskins/aws-python \
    cleanup-docker-images.py [REGISTRY_ID] [REPOSITORY_NAME]
```

### List ECR Images using local credentials file

```
docker run --rm -v ~/.aws:/root/.aws jdeskins/aws-python aws ecr list-images \
    --repository-name=[REPOSITORY_NAME] \
    --profile=[PROFILE_NAME]
```

### List Object Version Data from S3

```
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
    jdeskins/aws-python \
    list-versions.py -b bucket_name -p path_prefix
```


## Other Examples

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

Uses AWS environment variables to authenticate and get version data of all objects in the bucket
matching the prefix
