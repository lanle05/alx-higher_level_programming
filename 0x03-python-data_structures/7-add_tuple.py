#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    return sum_1, sum_2
