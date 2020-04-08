#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: aa.py
# First Edit: 2020-04-08
# Last Change: 08-Apr-2020.
"""
This scrip is for test

"""


def split_insuarance_or_not(raw_s):
    return raw_s.split("\r")


def all_number(raw_value):
    if isinstance(raw_value, int):
        return raw_value
    elif raw_value.startswith("*"):
        if isinstance(raw_value[1:], int):
            return all_number(int(raw_value[1:]))
        else:
            return all_number(raw_value[1:])
    else:
        try:
            return split_insuarance_or_not(raw_value)[0]
        except:
            print(raw_value)


def insure_only_number(raw_value, flag=False):
    try:
        return split_insuarance_or_not(raw_value)[1]
    except IndexError:
        if raw_value.startswith("*"):
            return insure_only_number(raw_value, flag=True)
        elif flag:
            return int(raw_value)
        else:
            return None


b = insure_only_number("50\r40")
print(b)
