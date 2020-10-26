#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: avange_graph.py
@time: 2020/10/27 2:02
@desc:
"""
import pygal
from numpy import mean

line_fir = [25.047, 22.805, 21.770, 16.858, 31.297, 21.748, 23.808, 20.637, 24.687, 20.270]
line_sec = [8.029, 10.085,9.351,11.698,10.890,12.737,10.455,10.299,8.931,8.261]
line_thr = [6.739,5.514,4.268,4.838,5.120,5.508,3.143,4.015,7.321,8.543]
line_four =  [4.872,3.820,6.684,7.581,8.957,2.562,5.639,5.168,6.013,9.405]
line_firv = [21.458,7.855,60.103,22.695,102.056,100.534,12.669,41.688,52.581,15.736]
line_six = [8.200, 12.217, 5.294, 7.356, 13.277, 9.908, 9.454, 6.109, 9.983, 10.964]

a_1 = mean(line_fir)
a_2 = mean(line_sec)
a_3 = mean(line_thr) * 10
a_4 = mean(line_four)
a_5 = mean(line_firv) * 10
a_6 = mean(line_six)

line_chart = pygal.HorizontalBar()
line_chart.title = 'the avange time of the question (/100)'
line_chart.add('BFS', a_1)
line_chart.add("DFS", a_2)
line_chart.add('IDS', a_3)
line_chart.add('A*_ONE', a_4)
line_chart.add('A*_TWO', a_5)
line_chart.add("A*_THREE",a_6)
line_chart.render_to_file('avange_chart.svg')