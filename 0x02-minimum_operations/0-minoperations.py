#!/usr/bin/python3
"""Alx coding interview challenge."""

def minOperations(n):
    """
    Returns an integer. If n is impossible to achieve, return 0
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    """print('H', end='')"""
    while done < n:
        if clipboard == 0:
            """init (the first copy all and paste)"""
            clipboard = done
            done += clipboard
            ops_count += 2
            """print('-(11)->{}'.format('H' * done), end='')"""
        elif n - done > 0 and (n - done) % done == 0:
            """copy all and paste"""
            clipboard = done
            done += clipboard
            ops_count += 2
            """print('-(11)->{}'.format('H' * done), end='')"""
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
            """print('-(01)->{}'.format('H' * done), end='')"""
    return ops_count