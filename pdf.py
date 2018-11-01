#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:57:30 2018

@author: jmobrecht
"""

import numpy as np

def pdf(k,c,x):
    # Note c is not mean wind speed.
    pdf = (k/c)*(x/c)**(k-1)*np.exp(-x/c)**k
    return pdf