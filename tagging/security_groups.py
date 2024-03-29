"""
Module: old_snapshots_ec2.py

This module contains a function that inserts tags into security groups.
"""
import boto3

def tag_security_group(ids_security_groups):
    aws_region = 'us-east-1'

    ec2_client = boto3.Session(region_name=aws_region).client('ec2')

    for sg_id in ids_security_groups:
        try:
            ec2_client.create_tags(
                Resources=[sg_id],
                Tags=[{'Key': 'KeyTag', 'Value': 'ValueTag'}]
            )
            print(f'Add Tag at Security Group {sg_id}')
        except Exception as e:
            print(f'Error tagging Security Group {sg_id}: {str(e)}')

if __name__ == "__main__":
    ids_security_groups = ['sg-1234','5678']
    tag_security_group(ids_security_groups)
