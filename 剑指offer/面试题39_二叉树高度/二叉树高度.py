# -*- coding: utf-8 -*-
__date__ = '2020/2/6 12:31'


class BTNode:
    """二叉树节点"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):
        return '{}'.format(self.elem)


class BTree:
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


def pre_creat():
    # 先序创建
    elem = int(input('请输入结点值（-1表示结束）：'))
    if elem == -1:
        bt = None
    else:
        node = BTNode(elem)
        bt = node
        bt.lchild = pre_creat()
        bt.rchild = pre_creat()
    return bt


def recur_height(root):
    # 递归求二叉树高度

    if root:
        lchild_height = recur_height(root.lchild)
        rchild_height = recur_height(root.rchild)
        max_height = lchild_height if lchild_height > rchild_height else rchild_height
        return max_height + 1
    else:
        return 0


def non_recur_height(root=None):
    # 非递归求二叉树高度

    height = 0
    if root is None:
        return height
    queue = [root]
    while queue:
        layer_len = len(queue)
        height += 1
        for _ in range(layer_len):
            cur = queue.pop(0)
            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)
    return height


def print_binary_tree(root=None, layer=0):
    # 层级打印

    if root is None:
        return
    print_binary_tree(root.lchild, layer+1)
    print('\t' * layer, end='')
    print(root.elem)
    print_binary_tree(root.rchild, layer+1)

    return


if __name__ == '__main__':
    binary_tree = BTree()

    # 层级建立二叉树
    for i in range(5):
        binary_tree.add(i)

    # 先序创建二叉树
    # binary_tree.root = pre_creat()

    print("二叉树的高度：", recur_height(binary_tree.root))
    print("非递归求二叉树高度为：", non_recur_height(binary_tree.root))

    # 打印展示
    print_binary_tree(binary_tree.root)
