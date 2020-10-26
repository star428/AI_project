#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: graph.py
@time: 2020/10/27 1:17
@desc:
"""
import pygal

line_chart = pygal.Line()
line_chart.title = 'the speed of the solve of the eightLayout'
line_chart.x_labels = map(str, range(0, 10))
line_chart.add('BFS/100', [25.047, 22.805, 21.770, 16.858, 31.297, 21.748, 23.808, 20.637, 24.687, 20.270])
line_chart.add('DFS/100',  [8.029, 10.085,9.351,11.698,10.890,12.737,10.455,10.299,8.931,8.261])
line_chart.add('IDS/10',  [6.739,5.514,4.268,4.838,5.120,5.508,3.143,4.015,7.321,8.543])
line_chart.add('A*_one/100',  [4.872,3.820,6.684,7.581,8.957,2.562,5.639,5.168,6.013,9.405])
line_chart.add('A*_two/10',  [21.458,7.855,60.103,22.695,102.056,100.534,12.669,41.688,52.581,15.736])
line_chart.add('A*_three/100',  [8.200,12.217,5.294,7.356,13.277,9.908,9.454,6.109,9.983,10.964])
line_chart.render()
line_chart.render_to_file('line_chart.svg')