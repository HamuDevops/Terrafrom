terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.13.0"
    }
  }
}
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "name" {
  ami           = "ami-0b09ffb6d8b58ca91"
  instance_type = "t3.micro"
  key_name = "terra"

  tags = {
    Name = "app.vm"
  }

}
