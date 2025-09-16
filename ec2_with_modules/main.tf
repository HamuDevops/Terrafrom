provider "aws" {
    region = "us-east-1"
  
}

module "ec2_instance" {
    source = "./modules/ec2_instance"
    ami = "ami-0b09ffb6d8b58ca91"
    instance_type = "t3.micro"
    subnet_id = "subnet-0424cb222f10b39ec"

}

