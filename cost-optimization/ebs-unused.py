import boto3
import sys

def get_unattached_volumes(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_volumes()

    unattached_volumes = []

    for volume in response['Volumes']:
        if len(volume['Attachments']) == 0:
            unattached_volumes.append(volume)

    return unattached_volumes

def calculate_storage_cost(volumes, storage_cost_per_gb):
    # WIP - Get storage_cost to aws-princing/ebs-pricing.py
    total_cost = 0
    for volume in volumes:
        size_gb = volume['Size']
        cost = size_gb * storage_cost_per_gb
        total_cost += cost

    return total_cost

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    region = sys.argv[1]

    # WIP - Get storage_cost to aws-princing/ebs-pricing.py
    #storage_cost_per_gb = float(sys.argv[2])

    unattached_volumes = get_unattached_volumes(region)

    if unattached_volumes:
        print("Unattached EBS volumes in the {} region: ".format(region))
        for volume in unattached_volumes:
            print(" - Volume ID:", volume['VolumeId'])
            print("   Size (GB):", volume['Size'])
            tags = volume.get('Tags', [])
            if tags:
                print("   TAGs:")
                for tag in tags:
                    print("     - {}: {}".format(tag['Key'], tag['Value']))
            else:
                print ("   No tags associated with this volume")
    else:
        print("No unattached EBS volumes found in the {} region.".format(region))

if __name__ == "__main__":
    main()
