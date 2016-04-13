#!/bin/bash

docker run -it -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION -v $(PWD)/data:/project/data jdeskins/aws-python
