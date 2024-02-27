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

**How the script Works**
1. The script makes use of the above tools installed such as python3, boto3 etc
2. It takes in the below 2 parameters such as "service_name" and "region"
3. It internally initiates a session and creates a client via boto to connect with the desired profile (in our case the default profile we setup initially)
4. It makes use of mapping as every service within AWS has a different resource calling method/type.
5. We make use of pagniation as few resource listing limits to a certain number.
6. We handle errors as well, which are caught at times when wrong service_name or regions are provided as part of the parameter input while we run the script.
7. Finally we can see the below example on how the script runs and gives us the desire o/p's. Screenshots are shared for reference. 

**Example below :**

For RDS : python3 /Path/To/oe.py rds us-east-1
For EC2 : python3 /Path/To/oe.py ec2 us-east-1
