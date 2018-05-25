#!/usr/bin/env python3
# -*- coding: utf-8 -*-
i = 0.001
cala = 0
totile = 180000
while (cala < 8000):
    cala = (180000 * i * (1 + i)**36) /( (1 + i)**36 - 1)
    print('每月还款', cala)
    print('利率：', i)
    i = i + 0.001
