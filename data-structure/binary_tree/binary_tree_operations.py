# -*- coding: utf-8 -*-
__date__ = '2020/1/8 15:45'

'''
二叉树相关操作
'''

from .binary_tree_creat import BTree, BTNode


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
    if root is None: return height
    queue = [root]
    while queue != []:
        layer_len = len(queue)
        height += 1
        for i in range(layer_len):
            cur = queue.pop(0)
            if cur.lchild: queue.append(cur.lchild)
            if cur.rchild: queue.append(cur.rchild)
    return height


def width(root=None):
    # 求二叉树宽度

    max_with = 0
    if root is None: return max_with
    queue = [root]
    while queue != []:
        layer_len = len(queue)
        if layer_len > max_with: max_with = layer_len
        for i in range(layer_len):
            cur = queue.pop(0)
            if cur.lchild: queue.append(cur.lchild)
            if cur.rchild: queue.append(cur.rchild)
    return max_with


def preorder(root=None):
    # 先序遍历二叉树

    if root is None:
        return
    else:
        print(root.elem, end=' ')
        preorder(root.lchild)
        preorder(root.rchild)


def inorder(root=None):
    # 中序遍历二叉树

    if root is None:
        return
    else:
        inorder(root.lchild)
        print(root.elem, end=' ')
        inorder(root.rchild)


def postorder(root=None):
    # 后序遍历二叉树

    if root is None:
        return
    else:
        postorder(root.lchild)
        postorder(root.rchild)
        print(root.elem, end=' ')


def print_binary_tree(root=None, layer=0):
    # 层级打印

    if root is None: return
    print_binary_tree(root.lchild, layer+1)
    print('\t' * layer, end='')
    print(root.elem)
    print_binary_tree(root.rchild, layer+1)


def swap(root=None):
    # 交换左右子树

    if root is None: return
    # swap(root.lchild)
    # tempt = root.rchild
    # root.rchild = root.lchild
    # root.lchild = tempt
    # # root.lchild, root.rchild = root.rchild, root.lchild
    # swap(root.rchild)


def pre_creat(bt):
    # 先序创建
    elem = int(input('请输入：'))
    if elem == 0:
        bt = None
    else:
        node = BTNode(elem)
        bt = node
        pre_creat(bt.lchild)
        pre_creat(bt.rchild)


if __name__ == '__main__':
    # binary_tree = BTree()
    # for i in range(7):
    #     binary_tree.add(i)
    # # preorder(binary_tree.root)
    # # print()
    # # inorder(binary_tree.root)
    # # print()
    # # postorder(binary_tree.root)
    # # print()
    # # print(recur_height(binary_tree.root))
    # # print(non_recur_height(binary_tree.root))
    # # print(width(binary_tree.root))
    # print_binary_tree(binary_tree.root)
    # swap(binary_tree.root)
    # print()
    # print()
    # print_binary_tree(binary_tree.root)

    binary_tree = BTree()
    pre_creat(binary_tree.root)
    print(binary_tree.root)
    print_binary_tree(binary_tree.root)
