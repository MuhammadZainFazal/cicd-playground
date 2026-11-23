# Infrastructure as Code example. Provisions the AWS pieces a pipeline would
# deploy to: a container registry (ECR). This is OPTIONAL and for later; it
# creates real AWS resources, so read docs/04-terraform.md first.

terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_ecr_repository" "app" {
  name                 = "${var.project}-${var.environment}"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
