#!/usr/bin/env python

import boto3
import getopt
import sys


def main(argv):
    bucket_name = ''
    prefix = ''

    try:
        opts, args = getopt.getopt(argv,"hb:p:",["bucket_name=", "prefix="])
    except getopt.GetoptError:
        print('list-versions.py -b <bucket_name> -p <prefix>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('list-versions.py -b <bucket_name> -p <prefix>')
            sys.exit()
        elif opt in ("-b", "--bucket_name"):
            bucket_name = arg
        elif opt in ("-p", "--prefix"):
            prefix = arg

    print('bucket_name=%s' % bucket_name)
    print('prefix=%s' % prefix)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    versions = bucket.object_versions.filter(Prefix=prefix)
    for obj in versions:
        print('%s|%s|%s' % (obj.key, obj.last_modified, obj.version_id))


if __name__ == "__main__":
    main(sys.argv[1:])
