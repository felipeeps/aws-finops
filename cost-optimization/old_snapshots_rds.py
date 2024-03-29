"""
Module: old_snapshots_rds.py

This module contains functions for discovery old snapshots on rds.
"""
import boto3
import sys
from datetime import datetime, timedelta, timezone

def get_old_rds_snapshots(region):
    rds = boto3.client('rds', region_name=region)
    # Get old date | Example using 1 year
    old_date = datetime.now(timezone.utc) - timedelta(days=365)
    response = rds.describe_db_snapshots()

    old_snapshots = [snapshot for snapshot in response['DBSnapshots'] if snapshot['SnapshotCreateTime'] < old_date]

    return old_snapshots

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    region = sys.argv[1]

    old_rds_snapshots = get_old_rds_snapshots(region)

    if old_rds_snapshots:
        print("Old RDS Snapshots in the {} region: ".format(region))
        for snapshot in old_rds_snapshots:
            print(" - ID:", snapshot['DBSnapshotIdentifier'])
            print("   Description:", snapshot.get('SnapshotCreateTime', 'N/A'))
            print("   Creation Date:", snapshot['SnapshotCreateTime'])
    else:
        print("No old RDS Snapshots found in the {} region.".format(region))

if __name__ == "__main__":
    main()
