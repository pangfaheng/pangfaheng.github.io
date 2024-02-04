terraform {
  required_providers {
    tencentcloud = {
      source  = "tencentcloudstack/tencentcloud"
      version = "1.81.72"
    }
  }

  backend "cos" {
    region   = "ap-guangzhou"
    bucket   = "bucket-for-terraform-state-1258798060"
    prefix   = "terraform/myproject/tc-ap-guangzhou/state"
    endpoint = "http://cos-internal.ap-guangzhou.tencentcos.cn"
  }
}

provider "tencentcloud" {
  region = "ap-guangzhou"
}
