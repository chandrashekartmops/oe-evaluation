variable "aws_profile" {}
variable "region" {}
variable "key_name" {}
variable "instance_types" {}
variable "vpc_security_group_ids" {}
variable "ami" {}
variable "instance_name" {
  type    = string
  default = "oe-test-eval"
}
