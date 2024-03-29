"""
Module: ebs-unused.py

This module contains functions for discovery ebs using GP2.
"""
import boto3

def list_gp2_volumes(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_volumes(Filters=[{'Name': 'volume-type', 'Values': ['gp2']}])

    gp2_volumes = response['Volumes']
    return gp2_volumes

def main():
    import sys
    if len(sys.argv) != 2:
        sys.exit(1)
    region = sys.argv[1]

    gp2_volumes = list_gp2_volumes(region)

    if gp2_volumes:
        print("GP2 volumes found in the {} region: ".format(region))
        for volume in gp2_volumes:
            print(" - Volume ID:", volume['VolumeId'])
            print("   Size (GiB):", volume['Size'])
            tags = volume.get('Tags', [])
            if tags:
                print("   Tags:")
                for tag in tags:
                    print("     - {}: {}".format(tag['Key'], tag['Value']))
            else:
                print("   No tags associated with this volume.")
    else:
        print("No GP2 volumes found in the {} region.".format(region))

if __name__ == "__main__":
    main()
