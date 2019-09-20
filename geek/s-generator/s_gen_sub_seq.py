#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/09/19 10:20
# @Author  : c0l0121
# @File    : s_gen_sub_seq.py
# @Desc    :


def sub_seq(target, source):
    source = iter(source)
    return all((i in source) for i in target)


def main():
    print(sub_seq([1, 6, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main()
