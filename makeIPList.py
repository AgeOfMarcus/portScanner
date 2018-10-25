#!/usr/bin/python3

from ipgen import rand_ipv4, rand_ipv6 as ipv4, ipv6
import argparse

def generate(amount,type):
	res = []
	for i in range(0,amount):
		if type == "IPv4":
			res.append(ipv4())
		elif type == "IPv6":
			res.append(ipv6())
		else:
			return 1
	return res

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-a","--amount",
		help=("Number of addresses to generate"),
		required=True,
		type=int)
	parser.add_argument(
		'-t','--type',
		help=("IP type (IPv4/IPv6)"),
		required=True)
	args = parser.parse_args()
	return args
	#CONT