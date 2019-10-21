from scapy.all import *
import os

ports = [4251, 4532, 4533]
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
timeout = 15


def open_access(ip):
    for i in ip:
        if i in ip:
            os.system('sh ipt | grep %s'.format() % ip)
            os.system('systemctl restart iptables.service')
        if existsinfw(ip):
            close_access(ips)
        elif not existsinfw(ips):
            print(('Opening %s' % ip))  # do something with this ip like:
            # noinspection PyStringFormat
            os.system('iptables -I INPUT 1 -s %s -p tcp --dport 22 -j ACCEPT'.format() % ip)
            break
        else:
            return False


def close_access(ip):
    print(('Closing %s' % ip))  # do something with this ip like:
    # noinspection PyStringFormat
    os.system('iptables -D INPUT -s %s -p tcp --dport 22 -j ACCEPT'.format() % ip)


def block_access(ip):
    for i in ip:
        if i in ip:
            os.system('sh ipt | grep %s'.format() % ip)
            os.system('systemctl restart iptables.service')
        if existsinfw(ips):
            close_access(ips)
        elif not existsinfw(ips):
            print(('Blocking %s' % ip))  # do something with this ip like:
            # noinspection PyStringFormat
            os.system('iptables -A INPUT -s %s -p tcp --dport 22 -j DROP'.format() % ip)
            break
        else:
            return False


p = sniff(iface='eno1',
          filter="tcp dst port 4251 or tcp dst port 4532 or tcp dst port 4533",
          count=3, timeout=15)
ips = p.res[0].getlayer('IP').src


def check():
    for i in range(3):
        if p.res[i].getlayer('TCP').getfieldval('dport') != ports[i]:
            return False
    return True


def baccess():
    wrong_count = 0
    while wrong_count < 3:
        if wrong_count == 3:
            wrong_count += 1
            print("Blocked! ")
        return True


def existsinfw(ip):
    fw = os.system('sh ipt | grep %s'.format() % ip)
    while True:
        if ips != fw:
            break
    return False


def main():
    while True:
        if check():
            open_access(ips)
            print("Your IP has been added to whitelist! ")
            break
        if baccess():
            block_access(ips)
            break


if __name__ == '__main__':
    main()
