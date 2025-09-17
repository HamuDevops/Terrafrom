provider "aws" {
    region = "us-east-1"
  
}

resource "aws_instance" "example" {
    ami = "ami-0b09ffb6d8b58ca91"
    instance_type = "t3.micro"

}
