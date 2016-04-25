#!/usr/bin/env python

import boto3
import sys


number_args = len(sys.argv)

if number_args < 3:
    print('Missing args: Pass repository name')
    sys.exit(1)

registryId = sys.argv[1]
repositoryName = sys.argv[2]
print("Cleaning up repository: %s" % repositoryName)

client = boto3.client('ecr')
response = client.list_images(registryId=registryId, repositoryName=repositoryName)

images = response.get('imageIds')
print('Total number of images: %d' % len(images))

images_to_delete = []

for image in images:
    imageDigest = image.get('imageDigest')
    imageTag = image.get('imageTag')

    if imageTag is None:
        print('No tag for image: %s' % image)
        images_to_delete.append({'imageDigest': imageDigest})

delete_response = client.batch_delete_image(
        registryId=registryId,
        repositoryName=repositoryName,
        imageIds=images_to_delete
)

print('delete_response=%s' % delete_response)

