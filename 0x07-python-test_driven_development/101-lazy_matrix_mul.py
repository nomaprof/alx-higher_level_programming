#!/usr/bin/python3
"""Use numpy to multiply two matices together"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Get the result of multiplying two matrices togehter

    Args:
        m_a (list of lists of ints/floats): Matrix 1
        m_b (list of lists of ints/floats): Matrix 2
    """

    return (np.matmul(m_a, m_b))
