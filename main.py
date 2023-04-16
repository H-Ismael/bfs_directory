"""
general file read and write utility based on bfs

"""

import os
from collections import deque


def bfs_dir(htransform, src_root_dir: str, dst_root_dir=None):
    """
    htrasform : represents the function used to manipulate files of the explored dirs (given the conditions set in
    htrasnform itself). src_root_dir : targeted parent/root directory. dst_root_dir : optional if None it will be
    assigned by default.
    """