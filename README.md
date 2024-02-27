**Overview**
This script allows you to list resources for various AWS services in different regions using the Boto3 library for Python. It provides a convenient way to retrieve resource information without the need for manual navigation through the AWS Management Console.

**Setup and Usage**
**Installation:**

Make sure you have Python installed on your system. You can download it from python.org.
Install the required dependencies by running pip install boto3 in your terminal.

**Configuration:**
Configure your AWS credentials using one of the following methods:

**AWS CLI:** Run aws configure in your terminal and follow the prompts to enter your Access Key ID, Secret Access Key, default region, and output format.
**Environment Variables:** Set the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_DEFAULT_REGION environment variables in your shell.
**IAM Role:** Ensure that your IAM role has the necessary permissions to access the AWS resources you want to list.

**Running the Script:**
python3 /Users/chandrashekar/Downloads/oe.py <SERVICE_NAME> <REGION>

**Example below :**
python3 /Path/To/oe.py rds us-east-1

