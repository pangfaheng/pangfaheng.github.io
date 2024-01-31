#! /usr/bin/bash

# 未挂载的磁盘列表
unmount_disks=()

# 已挂载的磁盘列表
mount_disk=`sudo lsblk --output NAME,TYPE,UUID,MOUNTPOINT|awk 'NR != 1 && $2 != "disk" && $3 != "" {print $1}'`

# 获取未挂载的磁盘列表
for device in `sudo lsblk --output NAME,TYPE,UUID,MOUNTPOINT|awk 'NR != 1 && $2 == "disk" && $3 == "" && $4 == "" {print $1}'`
do
    if [[ ! $mount_disk =~ $device ]];then
        unmount_disks[${#unmount_disks[@]}]="/dev/$device"
    fi
done

# 判断是否有硬盘未挂载
if [[ ${#unmount_disks[@]} -eq 0 ]];then
    exit 0
fi

# 循环初始化硬盘
for device in ${unmount_disks[*]}
do
    echo y | sudo mkfs -t ext4 ${device}
done

# 开机挂载硬盘
for ((i=0; i<${#unmount_disks[@]}; i++))
do
    if [[ $i == 0 ]];then
        data_path='/data'
    else
        data_path="/data"`expr ${i} + 1`
    fi
    if [[ ! -e ${data_path} ]];then
        sudo mkdir -p ${data_path}
    fi
    echo "${unmount_disks[$i]}    ${data_path}   ext4    defaults    1   2"| sudo tee -a /etc/fstab
done

# 挂载硬盘
sudo mount -a
exec_std=`echo $?`

if [[ $exec_std -eq 0 ]];then
    exit 0
else
    echo "挂载磁盘失败，请检查服务器"
    exit 1
fi