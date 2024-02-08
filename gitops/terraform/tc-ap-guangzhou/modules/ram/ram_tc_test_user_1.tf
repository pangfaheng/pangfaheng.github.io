# 创建用户：test_user_01
resource "tencentcloud_cam_user" "test_user_01" {
  name                = "test_user_01"
  remark              = "test_user_01"
  console_login       = false
  use_api             = true
  need_reset_password = false
  country_code        = "86"
  force_delete        = true
  tags = {
    project = "test",
  }
}

# 用户test_user_01绑定权限：ram_tc_policy_bill_1
resource "tencentcloud_cam_user_policy_attachment" "ram_at_test_user_01" {
  user_name = tencentcloud_cam_user.test_user_01.uid
  policy_id = tencentcloud_cam_policy.ram_tc_policy_bill_1.id
}
