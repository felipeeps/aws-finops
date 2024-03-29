import boto3

def get_stopped_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()

    stopped_instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'stopped':
                stopped_instances.append(instance['InstanceId'])

    return stopped_instances

def main():
    import sys
    if len(sys.argv) != 2:
        sys.exit(1)
    region = sys.argv[1]
    stopped_instances = get_stopped_instances(region)
    if stopped_instances:
        print("Stopped instances {}: ".format(region))
        for instance_id in stopped_instances:
            print(" -", instance_id)
    else:
        print("Not found Stopped instances {}.".format(region))

if __name__ == "__main__":
    main()
