#!/usr/bin/python3

import nmap
import os
os.system("tput clear;tput setaf 4")


scanner = nmap.PortScanner()


print("\t\t\t\t Welcome this is a Simple Scanner based on nmap")

ip = input("\n\n\n\t\t Please Enter Ip Address You want to scan:")
print("\t\t\tThe Ip you entered is :",ip)
type(ip)

resp = input("""\n\t\t Please Enter the scan you want to run 
                1.SYN ACK Scan
                2.UDP Scan
                3.Comprehensive Scan
                4.Exit\n""")

print("You have Selected option: ",resp)

if resp == '1':
    os.system("tput setaf 3")
    print("\t\t\tNmap Version:",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v','-sS')
    print(scanner.scaninfo())
    print("\t\t\tIp Status:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("\t\tOpen Ports:",scanner[ip]['tcp'].keys())

elif resp == '2':
    os.system("tput setaf 5")
    print("\t\t\tNmap Version:",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v','-sU')
    print(scanner.scaninfo())
    print("\t\t\tIp Status:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("\t\tOpen Ports:",scanner[ip]['udp'].keys())

elif resp == '3':
    os.system("tput setaf 6")
    print("\t\t\tNmap Version:",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v','-sS','-sV','-sC -A -O')
    print(scanner.scaninfo())
    print("\t\t\tIp Status:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("\t\tOpen Ports:",scanner[ip]['tcp'].keys())

elif resp == '4':
    exit()

