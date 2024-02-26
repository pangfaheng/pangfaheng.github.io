https://github.com/xyz690/multi-v2ray

source <(curl -sL https://multi.netlify.app/v2ray.sh) --zh


systemctl edit v2ray.service
[Service]
Environment=V2RAY_VMESS_AEAD_FORCED=false

systemctl restart v2ray.service


v2ray.vmess.aead.forced = false


You can still disable this security feature with environment variable v2ray.vmess.aead.forced = false