#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-26 09:39:51
# @Author  : Your Name (you@example.org)
# @Version : $id$

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",type=int)
# args = parser.parse_args()
# print args.square**2

# import argparse
# parser = argparse.ArgumentParser()
# # parser.add_argument("-v","--verbose", help="increase output verbosity",action="store_true")
# parser.add_argument("-v","--verbosity",choices=['0','1','2'], action="count", help="increase output verbosity",type=int)
# parser.add_argument("square",help="display a square of a given number",type=int)
# args = parser.parse_args()
# answer = args.square ** 2
# if args.verbosity == 2:
#     print 'the square of {} equals {}'.format(args.square, answer)
# elif args.verbosity == 1:
#     print "{} ^ 2 == {}".format(args.square,answer)
# else:
# 	print answer
# args = parser.parse_args()
# if args.verbose:
#   print "verbosity turned on"
# else:
# 	print "verbosity turned down"


# parser = argparse.ArgumentParser()
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# parser.add_argument("-v", "--verbosity", action="count", default=0)
# args = parser.parse_args()
# answer = args.x ** args.y
# if args.verbosity >= 2:
#      print "Running '{}'".format(__file__)
# if args.verbosity >= 1:
#      print "{}^{} == {}".format(args.x, args.y, answer)
# print answer

import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
       print answer
elif args.verbose:
       print "{} to the power {} equals {}".format(args.x, args.y, answer)
else:
       print "{}^{} == {}".format(args.x, args.y, answer)