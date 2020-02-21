# -*- coding: utf-8 -*-
__date__ = '2020/2/6 13:00'

class BTNode:
    """二叉树节点"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):
        return '{}'.format(self.elem)


class BTree(object):
    """二叉树"""

    def __init__(self, root=None):
        self.root = root

    def add(self, item=-1):
        # 层级建立二叉树

        node = BTNode(item)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)