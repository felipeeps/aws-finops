"""
Module: elastic_ips.py

This module contains functions for discovery ELPs not used.
"""
import boto3

def get_unused_elastic_ips(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_addresses()

    unused_elastic_ips = []

    for address in response['Addresses']:
        if 'InstanceId' not in address:
            unused_elastic_ips.append(address)

    return unused_elastic_ips

def main():
    import sys
    if len(sys.argv) != 2:
        sys.exit(1)
    region = sys.argv[1]

    unused_elastic_ips = get_unused_elastic_ips(region)

    if unused_elastic_ips:
        print("Unused Elastic IPs in the {} region: ".format(region))
        for ip in unused_elastic_ips:
            print(" - Elastic Public IP:", ip['PublicIp'])
            print("   ", ip['AllocationId'])
            print("   ", ip['NetworkInterfaceId'])
            print("   ", ip['PrivateIpAddress'])
            tags = ip.get('Tags', [])
            if tags:
                print("    TAGs:")
                for tag in tags:
                    print("     - {}: {}".format(tag['Key'], tag['Value']))
            else:
                print ("   No tags associated with this ELP")
    else:
        print("No unused Elastic IPs found in the {} region.".format(region))

if __name__ == "__main__":
    main()
