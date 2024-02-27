import sys
import boto3
from botocore.exceptions import ClientError

# Mapping of AWS service names to their resource types, describe methods, resource identifiers, and output names
SERVICE_MAPPING = {
    "ec2": {"describe_method": "describe_instances", "resource_key": "Reservations", "resource_identifier": "InstanceId", "resource_type": "Instances", "output_name": "InstanceId"},
    "s3": {"describe_method": "list_buckets", "resource_key": "Buckets", "resource_identifier": "Name", "resource_type": "S3 Buckets", "output_name": "Name"},
    "rds": {"describe_method": "describe_db_instances", "resource_key": "DBInstances", "resource_identifier": "DBInstanceIdentifier", "resource_type": "RDS Instances", "output_name": "DBInstanceIdentifier"},
    "lambda": {"describe_method": "list_functions", "resource_key": "Functions", "resource_identifier": "FunctionName", "resource_type": "Lambda Functions", "output_name": "FunctionName"},
    "iam": {"describe_method": "list_users", "resource_key": "Users", "resource_identifier": "UserName", "resource_type": "IAM Users", "output_name": "UserName"},
    "sqs": {"describe_method": "list_queues", "resource_key": "QueueUrls", "resource_identifier": "QueueUrl", "resource_type": "SQS Queues", "output_name": "QueueUrl"},
    "sns": {"describe_method": "list_topics", "resource_key": "Topics", "resource_identifier": "TopicArn", "resource_type": "SNS Topics", "output_name": "TopicArn"},
    "eks": {"describe_method": "list_clusters", "resource_key": "clusters", "resource_identifier": "clusterArn", "resource_type": "EKS Clusters", "output_name": "clusterArn"},
    "ecs": {"describe_method": "list_clusters", "resource_key": "clusterArns", "resource_identifier": "clusterArn", "resource_type": "ECS Clusters", "output_name": "clusterArn"},
    "dynamodb": {"describe_method": "list_tables", "resource_key": "TableNames", "resource_identifier": "TableName", "resource_type": "DynamoDB Tables", "output_name": "TableName"},
    "kinesis": {"describe_method": "list_streams", "resource_key": "StreamNames", "resource_identifier": "StreamName", "resource_type": "Kinesis Streams", "output_name": "StreamName"},
    "redshift": {"describe_method": "describe_clusters", "resource_key": "Clusters", "resource_identifier": "ClusterIdentifier", "resource_type": "Redshift Clusters", "output_name": "ClusterIdentifier"},
    "s3control": {"describe_method": "list_buckets", "resource_key": "Buckets", "resource_identifier": "Name", "resource_type": "S3 Buckets", "output_name": "Name"},
    "secretsmanager": {"describe_method": "list_secrets", "resource_key": "SecretList", "resource_identifier": "Name", "resource_type": "Secrets Manager Secrets", "output_name": "Name"},
    "sts": {"describe_method": "get_caller_identity", "resource_key": None, "resource_identifier": "Arn", "resource_type": "Caller Identity", "output_name": "Arn"},
    "transfer": {"describe_method": "list_servers", "resource_key": "Servers", "resource_identifier": "Arn", "resource_type": "Transfer Servers", "output_name": "Arn"},
    "waf": {"describe_method": "list_web_acls", "resource_key": "WebACLs", "resource_identifier": "WebACLId", "resource_type": "WAF Web ACLs", "output_name": "WebACLId"},
    "workspaces": {"describe_method": "describe_workspaces", "resource_key": "Workspaces", "resource_identifier": "WorkspaceId", "resource_type": "WorkSpaces", "output_name": "WorkspaceId"},
    # Add more services and their respective describe methods, resource types, and output names here
}

def list_resources(service_name, region_name):
    try:
        # Create a Boto3 client for the specified service in the specified region
        client = boto3.client(service_name, region_name=region_name)

        # Get describe method, resource key, resource identifier, resource type, and output name from the service mapping
        describe_method = SERVICE_MAPPING[service_name]["describe_method"]
        resource_key = SERVICE_MAPPING[service_name]["resource_key"]
        resource_identifier = SERVICE_MAPPING[service_name]["resource_identifier"]
        resource_type = SERVICE_MAPPING[service_name]["resource_type"]
        output_name = SERVICE_MAPPING[service_name]["output_name"]

        # Initialize empty list to hold all resources
        all_resources = []

        # Paginator for handling pagination
        paginator = client.get_paginator(describe_method)
        for page in paginator.paginate():
            if resource_key:
                resources = page.get(resource_key)
            else:
                resources = [page]

            # Append resources to the list
            all_resources.extend(resources)

        # Print the resources
        if all_resources:
            print(f"Resources for {service_name.upper()} ({resource_type}) in {region_name}:")
            if service_name == "ec2":
                # Print only instance IDs for EC2 instances
                for reservation in all_resources:
                    for instance in reservation.get("Instances", []):
                        instance_id = instance.get(resource_identifier)
                        print(f"{output_name}: {instance_id}")
            else:
                # Print resource identifiers for other services
                for resource in all_resources:
                    resource_value = resource.get(resource_identifier)
                    print(f"{output_name}: {resource_value}")
        else:
            print(f"No resources found for {service_name.upper()} ({resource_type}) in {region_name}")

    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRegion':
            print(f"Invalid region '{region_name}' provided.")
        else:
            print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <service_name> <region_name>")
        sys.exit(1)

    service_name = sys.argv[1].lower()
    region_name = sys.argv[2]

    list_resources(service_name, region_name)
