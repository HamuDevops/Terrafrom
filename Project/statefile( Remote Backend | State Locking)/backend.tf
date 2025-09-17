terraform {
  backend "s3" {
    bucket = "hamuza-terraform"
    key = "hamuza/terraform.tfstate"
   region = "us-east-1"
   encrypt = true
   
 }
}