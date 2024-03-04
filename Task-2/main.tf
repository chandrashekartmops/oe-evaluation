terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "oe-test"  
  region  = "eu-north-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-02d0a1cbe2c3e5ae4"
  instance_type = "t3.micro"
  key_name = "oe-test"
  vpc_security_group_ids = [ "sg-0c15e710651b908e9" ]

  tags = {
    Name = "oe-test-eval"
  }
}
