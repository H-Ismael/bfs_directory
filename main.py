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

    # setting a que to apply bfs on the directory try
    paths_q = deque([src_root_dir])
    visited = set()

    while paths_q:
        src_current_f = paths_q.popleft()
        print('current source folder', src_current_f)
        src_current = src_current_f.strip('/')
        if dst_root_dir is None:
            # if the destination is not specified it will generate an exact similar dir scheme while doing manipulations on the file (this is not complsory if the used method does not require it in the first place)
            dst_current_f = src_current_f.replace(src_current[-1], f'transformed_{src_current[-1]}')
        elif type(dst_root_dir) is not str:
            print("second arg must be a str")
        else:
            dst_current_f = dst_root_dir

        if os.path.isdir(src_current_f):
            if not os.path.exists(dst_current_f):
                os.mkdir(dst_current_f)
            for children in os.listdir(src_current_f):
                src_children_path = f'{src_current_f}/{children}'
                dst_children_path = f'{dst_current_f}/{children}'
                if not os.path.isdir(src_children_path):
                    htransform(src_children_path, dst_children_path)
                if src_children_path not in visited:
                    paths_q.append(src_children_path)
                    visited.add(src_children_path)