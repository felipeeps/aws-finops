import boto3
import sys
from datetime import datetime, timedelta

def get_old_snapshots(region):
    ec2 = boto3.client('ec2', region_name=region)
    # Get old date | Example using 1 year
    old_date = datetime.now() - timedelta(days=365)

    response = ec2.describe_snapshots(OwnerIds=['self'])
    old_snapshots = [snapshot for snapshot in response['Snapshots'] if snapshot['StartTime'] < old_date]

    return old_snapshots

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    region = sys.argv[1]
    old_snapshots = get_old_snapshots(region)

    if old_snapshots:
        print("Old Snapshots in the {} region: ".format(region))
        for snapshot in old_snapshots:
            print(" - ID:", snapshot['SnapshotId'])
            print("   Description:", snapshot.get('Description', 'N/A'))
            print("   Creation Date:", snapshot['StartTime'])
    else:
        print("No old Snapshots found in the {} region.".format(region))

if __name__ == "__main__":
    main()
