#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: BFS_solve.py
@time: 2020/10/26 20:56
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


def the_BFS_solve(srcLayout):
    dict_Layout = {}
    if AccessibilityOfSolve(srcLayout):
        dict_Layout[srcLayout] = -1
        # 初始化字典
        stack_Layout = [srcLayout]
        # 将状态保存在栈中
        while len(stack_Layout) > 0:
            currentLayout = stack_Layout.pop(0) # 与dfs不同之处，改为队列即可
            if currentLayout == destLayout:
                break
            # 寻找0的位置
            zeroPosition = currentLayout.index("0")
            # 下面列表为可交换的位置的集合（也就是哪个位置可以变换）
            list_can_swap = canSwapDict[zeroPosition]
            for position in list_can_swap:
                newLayout = swapLayout(currentLayout, position, zeroPosition)

                if dict_Layout.get(newLayout) == None:  # 判断交换后是否查询
                    dict_Layout[newLayout] = currentLayout
                    stack_Layout.append(newLayout)  # 存入集合

        # 上面字典保存的都是父子节点对
        lst_steps = [currentLayout]
        while dict_Layout[currentLayout] != -1:  # 树的父节点的值
            currentLayout = dict_Layout[currentLayout]
            lst_steps.append(currentLayout)  # 找到回溯路径
        lst_steps.reverse()  # 反向排序找到
        return lst_steps


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
    totalNum = 100
    startTime = time.time()
    for current_num in range(totalNum):
        src = mkList()
        print(src[:3])
        print(src[3:6])
        print(src[6:])
        if AccessibilityOfSolve(src):
            steps = the_BFS_solve(src)
            print("steps is : " + str(len(steps)))
        else:
            print("false")
        print("--------------")
    endTime = time.time()
    print("all the time is" + str(endTime - startTime))


