import boto3

# WIP - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html
# https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/eu-west-1/index.json
# https://github.com/lyft/awspricing


def get_ebs_storage_price(region):
    # WIP
    pricing = boto3.client('pricing', region_name=region)
    response = pricing.get_price_list_file_url()

    print(response)

def main():
    # WIP
    get_ebs_storage_price('us-east-1')

if __name__ == "__main__":
    main()
