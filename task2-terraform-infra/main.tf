terraform {
  required_version = ">= 1.0.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

resource "local_file" "infra_config" {
  content  = "scalable_infrastructure=active\nprovisioner=terraform\nenvironment=production\n"
  filename = "${path.module}/terraform_output.conf"
}

output "infra_status" {
  value = "Scalable infrastructure provisioned successfully using Terraform!"
}
