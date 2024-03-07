#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_GraphDroid.py
@Time    :   2021/10/12 14:42:28
@Author  :   Yiling He
@Version :   1.0
@Contact :   heyilinge0@gmail.com
@License :   (C)Copyright 2021
@Desc    :   None
'''

# here put the import lib
import unittest
from examples.android_malware_detection import GraphDroidAnalyzer


class TestGraphDroid(unittest.TestCase):
    def test_GraphDroid(self):
        snippet_subgraphs = GraphDroidAnalyzer(apkpath="/mnt/9699a7bf-7770-4a52-8da1-494497c49166/AndroZoo50k/00A0BC07048FDF0E1669D9940DED6A9A36029DCC76B2E1C6C3D554DC0B5E5AAE.apk").features
        for snippet in snippet_subgraphs:
            print(snippet)