#!/usr/bin/env python
# encoding: utf-8
"""
@author: star428
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited 
@contact: yewang863@gmail.com
@software: pycharm
@file: A_solve_two.py
@time: 2020/10/26 23:23
@desc: 一般的有不同
"""
#!/usr/bin/env python
# encoding: utf-8
import random
import time

destLayout = "123456780"

dict_layouts = {}  # 对象父子级关系
dict_layouts_deep = {}  # 对象深度(也就是gn的值）
dict_layouts_fn = {}  # 对象的fn值

canSwapPoint = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
                6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}


def swap_layout(srcLayout, i, j, deep):
    if i > j:
        i, j = j, i
    outPutLayout = srcLayout[:i] + srcLayout[j] + srcLayout[i + 1:j] + \
                   srcLayout[i] + srcLayout[j + 1:]
    fn = deep + 1 + hn(outPutLayout)
    return outPutLayout, fn


# 此时求解估计值hn
def hn(srcLayout):
    sum = 0
    for i in range(9):
        if srcLayout[i] is not destLayout[i]:
            sum += 1
            # 此时计数的为每个位置不相同的个数
    return sum


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


def the_A_solve(srcLayout):
    if AccessibilityOfSolve(srcLayout):
        dict_layouts[srcLayout] = -1
        dict_layouts_deep[srcLayout] = 0
        dict_layouts_fn[srcLayout] = 0 + hn(srcLayout)
        stack_layout = []
        gn = 0  # 深度值为0
        stack_layout.append(srcLayout)  # 将当前状态保存到列表
        while len(stack_layout) > 0:
            currentLayout = min(dict_layouts_fn, key=dict_layouts_fn.get)
            del dict_layouts_fn[currentLayout]
            stack_layout.remove(currentLayout)

            if currentLayout == destLayout:
                break

            zeroPosition = currentLayout.index('0')
            list_can_move = canSwapPoint[zeroPosition]
            for position in list_can_move:
                newLayout, fn = swap_layout(currentLayout, position,
                                            zeroPosition,
                                            dict_layouts_deep[currentLayout])
                if dict_layouts.get(newLayout) == None:
                    dict_layouts[newLayout] = currentLayout
                    dict_layouts_deep[newLayout] = dict_layouts_deep[
                                                       currentLayout] + 1
                    dict_layouts_fn[newLayout] = fn
                    stack_layout.append(newLayout)

        lst_steps = []
        lst_steps.append(currentLayout)
        while dict_layouts[currentLayout] != -1:  # 存入路径
            currentLayout = dict_layouts[currentLayout]
            lst_steps.append(currentLayout)
        lst_steps.reverse()
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
    totalNum = 10
    startTime = time.time()
    for current_num in range(totalNum):
        src = mkList()
        print(src[:3])
        print(src[3:6])
        print(src[6:])
        if AccessibilityOfSolve(src):
            steps = the_A_solve(src)
            print("steps is : " + str(len(steps)))
            dict_layouts = {}  # 对象父子级关系
            dict_layouts_deep = {}  # 对象深度(也就是gn的值）
            dict_layouts_fn = {}  # 对象的fn值
        else:
            print("false")
        print("--------------")
    endTime = time.time()
    print("all the time is" + str(endTime - startTime))
