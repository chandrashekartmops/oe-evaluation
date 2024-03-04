
resource "aws_instance" "app_server" {
  ami = var.ami
  instance_type = var.instance_types
  key_name = var.key_name
  vpc_security_group_ids = var.vpc_security_group_ids

  tags = {
    Name = var.instance_name
  }
}
