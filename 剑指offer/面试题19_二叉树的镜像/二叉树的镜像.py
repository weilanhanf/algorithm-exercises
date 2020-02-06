# -*- coding: utf-8 -*-
__date__ = '2020/2/6 12:39'


class BTNode:
    """二叉树节点"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):  # 输出节点时展示结点的值
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


def print_binary_tree(root=None, layer=0):
    # 层级打印

    if root is None:
        return
    print_binary_tree(root.lchild, layer+1)
    print('\t' * layer, end='')
    print(root.elem)
    print_binary_tree(root.rchild, layer+1)

    return


def mirror_swap(root=None):
    if root is None:
        return None
    else:
        root.rchild, root.lchild = mirror_swap(root.lchild), mirror_swap(root.rchild)
    return root


if __name__ == '__main__':
    binary_tree = BTree()

    # 层级建立二叉树
    for i in range(5):
        binary_tree.add(i)

    # 层级打印二叉树展示
    print_binary_tree(binary_tree.root)

    print("反转左右子树之后：")
    binary_tree.root = mirror_swap(binary_tree.root)
    print_binary_tree(binary_tree.root)