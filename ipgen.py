#!/usr/bin/python3

from random import getrandbits
from ipaddress import IPv4Address, IPv6Address
import argparse

def rand_ipv4():
	bits = getrandbits(32) # integer with 32 random bits
	addr = IPv4Address(bits) # IPv4Address object
	addr_str = str(addr)
	return addr_str
def rand_ipv6():
	bits = getrandbits(128)
	addr = IPv6Address(bits)
	addr_str = addr.compressed
	return addr_str

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--v6",
		help=("Generate an IPv6 address"),
		action="store_true")
	parser.add_argument(
		"--v4",
		help=("Generate an IPv4 Address [Default]"),
		action="store_true")
	args = parser.parse_args()
	return args
def main(args):
	if args.v6:
		print(rand_ipv6())
	else:
		print(rand_ipv4())
	return 0

if __name__ == "__main__":
	exit(main(parse_args()))