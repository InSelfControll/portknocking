Requirments:
python 2 or 3
Must be on linux fedora / centos / debian based systems.
pip install scapy
pip install
Make sure iptables is up and runing 
This software only for checking the port knocking server.
apt-get install knockd
or for redhat / centos / fedora 
yum install knocked
or
rpm -ivh https://rpmfind.net/linux/opensuse/tumbleweed/repo/oss/x86_64/knockd-0.7-2.8.x86_64.rpm
for mac
https://apps.apple.com/us/app/knock-unlock-your-mac-without-password-using-your-iphone/id692929970

Commands to preform:
iptables -I INPUT -p tcp -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -I INPUT -p icmp -j ACCEPT
iptables –A INPUT –j REJECT
knock –v server_ip 2222 3333 4444 ;ssh server_ip
