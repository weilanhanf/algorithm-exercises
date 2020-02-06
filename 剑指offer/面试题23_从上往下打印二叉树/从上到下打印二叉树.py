# -*- coding: utf-8 -*-
__date__ = '2020/2/6 13:13'


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


def print_from_top_to_bottom(root=None):
    # 层级遍历二叉树，这与层级建立二叉树时一致
    if root is None:
        return []
    else:
        res = []  # 用res存储遍历结果
        queue = [root]  # 模拟队列
        while queue:
            node = queue.pop(0)
            res.append(node.elem)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    return res


if __name__ == '__main__':
    binary_tree = BTree()

    # 层级建立二叉树
    for i in range(5):
        binary_tree.add(i)

    print("层级遍历二叉树：", print_from_top_to_bottom(binary_tree.root))
