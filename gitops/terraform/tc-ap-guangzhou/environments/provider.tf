terraform {
  required_providers {
    tencentcloud = {
      source  = "tencentcloudstack/tencentcloud"
      version = "1.81.72"
    }
  }

  backend "cos" {
    region   = "ap-guangzhou"
    bucket   = "myproject-1256008400"
    prefix   = "terraform/myproject/tc-ap-guangzhou/state"
    endpoint = "https://myproject-1256008400.cos.ap-guangzhou.myqcloud.com"
  }
}

provider "tencentcloud" {
  region = "ap-guangzhou"
}
