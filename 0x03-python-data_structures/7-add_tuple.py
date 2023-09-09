#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aa1 = tuple_a[0] if len(tuple_a) > 0 else 0
    aa2 = tuple_a[1] if len(tuple_a) > 1 else 0
    bb1 = tuple_b[0] if len(tuple_b) > 0 else 0
    bb2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (aa1 + bb1, aa2 + bb2)
