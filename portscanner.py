#!/usr/bin/python3

import socket, argparse

def check(ip,port):
        s = socket.socket()
        s.settimeout(1)
        try:
                s.connect((ip,port))
                return True
        except:
                return False

def scan_addrs(addrs,v=True):
        res = {}
        for addr in addrs:
                ip, port = addr.split(":")
                res[addr] = check(ip,int(port))
                if v: print("Result for [%s]: %s" % (
                        addr, str(res[addr])
                ))
        return res

def scan_ports(ip,ports,v=True):
        res = {}
        for port in ports:
                port = int(port)
                res[port] = check(ip,port)
                if v: print("Result for [%s]: %s" % (
                        str(port), str(res[port])
                ))
        return res

def scan_ips(ips,port,v=True):
        res = {}
        for ip in ips:
                res[ip] = check(ip,port)
                if v: print("Result for [%s]: %s" % (
                        ip, str(res[ip])
                ))
        return res

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-f","--file",
		help=("Read from file. Eg: --file addrs.txt. Format should be <ip:port> if -i and -p not specified, \
			<port> if -i specified, \
			<ip> if -p specified."),
		required=True)
	parser.add_argument(
		"-i","--ip",
		help=("Target IP. Eg: --ip 127.0.0.1"))
	parser.add_argument(
		"-p","--port",
		help=("Target port. Eg: --port 8080"))
	args = parser.parse_args()
	return args

def show_true(res):
	for i in res:
		if res[i]:
			print(i)

def cli(args):
	try:
		if not args.ip is None:
			ports = open(args.file,"r").read().split("\n")
			res = scan_ports(args.ip,ports,v=False)
			print(res)
			return 0
		elif not args.port is None:
			ips = open(args.file,"r").read().split("\n")
			res = scan_ips(ips,args.port,v=False)
			print(res)
			return 0
		else:
			addrs = open(args.file,"r").read().split("\n")
			res = scan_addrs(addrs,v=False)
			print(res)
			return 0
	except Exception as e:
		print("Error: "+str(e))	


def mainMenu():
        fin = 0
        while True:
                choice = input('''
        1. Scan a list of addresses (ip:port)
        2. Scan one ip with a list of ports (port)
        3. Scan one port on a list of ips (ip)
        4. Exit

        Your choice: ''')

                if choice == "1":
                        fn = input("Filename: ")
                        try:
                                addrs = open(fn,"r").read().split("\n")
                        except Exception as e:
                                print("Error: "+str(e))
                                fin = 1
                        print("Starting scan...\n")
                        res = scan_addrs(addrs)
                        print("\n\nPostitive results:")
                        for i in res:
                                if res[i]:
                                        print(i)
                        fin = 0
                elif choice == "2":
                        fn = input("Filename: ")
                        try:
                                ports = open(fn,"r").read().split("\n")
                        except Exception as e:
                                print("Error: "+str(e))
                                fin = 1
                        ip = input("Target IP: ")
                        print("Starting scan...\n")
                        res = scan_ports(ip,ports)
                        print("\n\nPostitive results:")
                        for i in res:
                                if res[i]:
                                        print(i)
                        fin = 0
                elif choice == "3":
                        fn = input("Filename: ")
                        try:
                                ips = open(fn,"r").read().split("\n")
                        except Exception as e:
                                print("Error: "+str(e))
                                fin = 1
                        port = int(input("Target port: "))
                        print("Starting scan...\n")
                        res = scan_ips(ips,port)
                        print("\n\nPostitive results:")
                        for i in res:
                                if res[i]:
                                        print(i)
                        fin = 0
                elif choice == "4":
                        break
                else:
                        print("Invalid Option")
        return fin

if __name__ == "__main__":
        exit(cli(parse_args()))