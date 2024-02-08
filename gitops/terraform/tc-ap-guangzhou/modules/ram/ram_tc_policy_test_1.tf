# 项目管理权限，命名为：ram_云厂商_policy_项目名称_编号
resource "tencentcloud_cam_policy" "ram_tc_policy_test_1" {
  name        = "ram_tc_policy_test_1"
  document    = <<EOF
{
    "statement": [
        {
            "action": [
                "cvm:*",
                "vpc:*",
                "tag:*",
                "monitor:*",

            ],
            "effect": "allow",
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "proj&test"
                    ]
                }
            }
        },
        {
            "action": [
                "cam:ListUsersForGroup",
                "cam:ListGroups",
                "cam:GetGroup",
                "cam:MonitorGetProject"
            ],
            "effect": "allow",
            "resource": [
                "*"
            ]
        }
    ],
    "version": "2.0"
}
EOF
  description = "test项目管理权限"
}
