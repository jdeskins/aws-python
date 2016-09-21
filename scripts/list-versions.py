#!/usr/bin/env python

import argparse
import boto3


'''
Description:
List versions of objects in an S3 bucket path

Example:
list-versions.py -b <bucket_name> -p <prefix>
'''


def main():
    # Get args passed into the script
    parser = argparse.ArgumentParser(description='List all versions of objects in a bucket, filtered by prefix.')
    parser.add_argument('-b','--bucket', help='bucket name', required=True)
    parser.add_argument('-p','--prefix',help='path within bucket to filter objects', required=False)
    args = parser.parse_args()

    bucket_name = args.bucket
    prefix = args.prefix or ''

    print('bucket_name=%s' % bucket_name)
    print('prefix=%s' % prefix)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    total_mb = 0

    versions = bucket.object_versions.filter(Prefix=prefix)
    for obj in versions:
        if obj.size:
            size = float(obj.size)/1024/1024
        else:
            size = 0
        total_mb += size
        print('%s|%s|%s|%sMB' % (obj.key, obj.last_modified, obj.version_id, size))

    print('==================')

    if total_mb > 1024:
        print('Total: %.1f GB' % (total_mb/1024))
    else:
        print('Total: %.1f MB' % total_mb)

if __name__ == "__main__":
    main()
