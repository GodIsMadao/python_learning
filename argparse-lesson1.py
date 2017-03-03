#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-23 16:37:27
# @Author  : Your Name (you@example.org)
# @Version : $id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print args.echo




