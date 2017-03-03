#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 15:12:24
# @Author  : Your Name (you@example.org)
# @Version : $id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from io import StringIO
f = StringIO()
f.write('hello'.decode('gbk'))
print(f.getvalue());