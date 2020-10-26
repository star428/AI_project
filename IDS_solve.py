#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: IDS_solve.py
@time: 2020/10/26 21:23
@desc:
"""
import random
import time

canSwapDict = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
               3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
               6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
# 在每一点的值可移动到的位置
destLayout = "123456780"


def swapLayout(srcLayout, i, j):
    if i > j:
        i, j = j, i
    output = srcLayout[:i] + srcLayout[j] + srcLayout[i + 1:j] + srcLayout[i] \
             + srcLayout[j + 1:]
    return output


def AccessibilityOfSolve(srcLayout):
    """用字符串表示八数码问题的状态，其中0表示未占位"""
    count = 0
    # 奇偶性判别所用到的冲突计数
    for index in range(8):
        if srcLayout[index] == '0':
            continue
        for y in range(index + 1, 9):
            if srcLayout[index] > srcLayout[y] != '0':
                count += 1

    if count % 2 != 0:
        return False
    else:
        return True


def the_main_IDS_solve(srcLayout, depth):
    dict_Layout = {}
    bFound = False
    if AccessibilityOfSolve(srcLayout):
        dict_Layout[srcLayout] = [-1, 0]  # 加入depth量，前一个表示其父节点
        # 后一个为其树的深度
        stack_Layout = [srcLayout]
        # 将状态保存在栈中
        while len(stack_Layout) > 0:
            currentLayout = stack_Layout.pop()
            if currentLayout == destLayout:
                bFound = True
                break
            zeroPosition = currentLayout.index("0")
            list_can_swap = canSwapDict[zeroPosition]
            for position in list_can_swap:
                newLayout = swapLayout(currentLayout, position, zeroPosition)

                if dict_Layout.get(newLayout) == None and \
                        dict_Layout[currentLayout][1] < depth:
                    dict_Layout[newLayout] = \
                        [currentLayout, dict_Layout[currentLayout][1] + 1]
                    stack_Layout.append(newLayout)

    return bFound


def the_IDS_solve(srcLayout, depth):
    isFound = False
    isFound = the_main_IDS_solve(srcLayout, depth)
    while not isFound:
        depth += 1
        isFound = the_main_IDS_solve(srcLayout, depth)

    return depth


def mkList():
    a = []
    totalList = list(range(0, 9))
    num = 9
    while num > 0:
        x = random.randint(0, len(totalList) - 1)
        curNum = totalList[x]
        a.append(curNum)
        totalList.pop(x)
        num -= 1

    src = ""
    for i in range(len(a)):
        src += str(a[i])

    return src

if __name__ == "__main__":
    totalNum = 10
    startTime = time.time()
    for current_num in range(totalNum):
        src = mkList()
        print(src[:3])
        print(src[3:6])
        print(src[6:])
        if AccessibilityOfSolve(src):
            the_depths = the_IDS_solve(src, 1)
            print("the depths is : " + str(the_depths))
        else:
            print("false")
        print("--------------")
    endTime = time.time()
    print("all the time is" + str(endTime - startTime))
