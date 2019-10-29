#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 2019
@author: Nathan de Lara <ndelara@enst.fr>
"""

import unittest

import numpy as np

from sknetwork.utils import Ward


class TestKMeans(unittest.TestCase):

    def setUp(self):
        self.x = np.random.randn(10, 3)

    def test_kmeans(self):
        ward = Ward()
        ward.fit(self.x)
        self.assertEqual(ward.dendrogram_.shape, (self.x.shape[0]-1, 4))
