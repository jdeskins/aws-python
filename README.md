# aws-python

Simple Docker container that provides workspace to run aws commandline tools in python.

Requires access key and secret to be set in environment variables or attaching the ~/.aws volume when running the
container.

To set environment variables:
```
export AWS_ACCESS_KEY_ID=[YOUR_AWS_ACCESS_KEY_ID]
export AWS_SECRET_ACCESS_KEY=[YOUR_AWS_SECRET_ACCESS_KEY]
```

To use existing aws credentials on host:
Add `-v ~/.aws:/root/.aws` to the docker run command if it doesn't already have it.

## Run local scripts from container environment
Use the following to launch container with your local files.  Puts you at bash prompt within project directory.
From there you can run/modify local python files while using the container environment with boto3.
```
docker run -it --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
    -v /path-to-local-files:/project jdeskins/aws-python
```


## Available Scripts

### Delete Untagged ECR Images

When a docker image is tagged as "latest" in ECR, the previous version tagged "latest" still exists but
is no longer tagged.  That container is cached for possible later re-use.
This script will remove all untagged containers from the repo to conserve space for a given
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

Uses AWS environment variables to authenticate and get version data of all objects in the bucket
matching the prefix.

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

To automatically execute the docker login for ECR, run:
```
$(docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
      jdeskins/aws-python aws ecr get-login)
```
