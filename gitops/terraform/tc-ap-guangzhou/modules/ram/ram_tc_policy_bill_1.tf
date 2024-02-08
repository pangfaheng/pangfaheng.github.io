resource "tencentcloud_cam_policy" "ram_tc_policy_bill_1" {
  name        = "ram_tc_policy_bill_1"
  document    = <<EOF
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "finance:*"
            ],
            "effect": "allow",
            "resource": [
                "qcs::cvm:::*",
                "qcs::vpc:::*",
                "qcs::clb:::*",
                "qcs::cdb:::*"
            ]
        }
    ]
}
EOF
  description = "支付订单权限"
}
