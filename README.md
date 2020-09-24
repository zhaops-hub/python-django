## python django 项目

> 这是我的联系项目

## 遇到的问题

​

1. ​	docker 容器内连不上网的原因，centos7 内核开启ip转发

>  sudo echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
>  sudo sysctl -p
>  sudo systemctl restart docker