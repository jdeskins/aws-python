#!/usr/bin/env python

from datetime import datetime
import boto3

'''
Prints list of ELBs with no requests during 7 day range.
StartTime and EndTime is currently hard-coded and should probably be dynamic.
Returns list of instances attached to the ELB
'''


def main():
    client = boto3.client('elb')
    cw_client = boto3.client('cloudwatch')

    response = client.describe_load_balancers()

    descriptions = response["LoadBalancerDescriptions"]
    for elb in descriptions:
        elb_name = elb["LoadBalancerName"]
        stats = cw_client.get_metric_statistics(
            Namespace='AWS/ELB',
            MetricName='RequestCount',
            Dimensions=[
                {'Name': 'LoadBalancerName', 'Value': elb_name},
            ],
            StartTime=datetime(2017, 4, 4),
            EndTime=datetime(2017, 4, 11),
            Period=3600,
            Statistics=['Sum']
        )

        if len(stats["Datapoints"]) == 0:
            tags_response = client.describe_tags(
                LoadBalancerNames=[elb_name]
            )
            project_name = "N/A"
            environment = "N/A"

            tags = tags_response['TagDescriptions'][0]['Tags']
            for tag in tags:
                if tag['Key'] == 'Project':
                    project_name = tag['Value']
                if tag['Key'] == 'Environment':
                    environment = tag['Value']

            print("\n====================================")
            print("Project: " + project_name + " (" + environment + ")")
            print("No Requests on ELB: " + elb_name)
            print("---> Instances: " + str(elb["Instances"]))
        # print(stats)


if __name__ == '__main__':
    main()
