#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# here put the import lib
import unittest
from examples.android_malware_detection import MalGraphAnalyzer

from . import format_print, timer

class TestMalGraph(unittest.TestCase):
    @timer
    def test_MalGraph(self):
        graph = MalGraphAnalyzer(apkpath="/mnt/9699a7bf-7770-4a52-8da1-494497c49166/AndroZoo50k/00A0BC07048FDF0E1669D9940DED6A9A36029DCC76B2E1C6C3D554DC0B5E5AAE.apk").features
        print(graph)