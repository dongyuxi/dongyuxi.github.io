---
layout: post
title: LeetCode 103 - Binary Tree Zigzag Level Order Traversal - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem103-binary-tree-zigzag-level-order-traversal
---
***<https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/>***
<!--more-->
```java
/**
 * Given a binary tree, return the zigzag level order traversal of its nodes' values.
 * (ie, from left to right, then right to left for the next level and alternate between).
 * 
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *   3
 *  / \
 * 9  20
 *   /  \
 *  15   7
 *  return its bottom-up level order traversal as:
 * [
 *  [3],
 *  [9,20],
 *  [15,7]
 * ]
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> listlist = new ArrayList<ArrayList<Integer>>();
        LinkedList<TreeNode> currentLevel = new LinkedList<TreeNode>();
        int level = 0;
        if (root != null)
            currentLevel.add(root);
        while (!currentLevel.isEmpty()) {
            LinkedList<TreeNode> nextLevel = new LinkedList<TreeNode>();
            ArrayList<Integer> list = new ArrayList<Integer>();
            for (TreeNode node : currentLevel) {
                list.add(node.val);
                if (node.left != null)
                    nextLevel.add(node.left);
                if (node.right != null)
                    nextLevel.add(node.right);
            }
            if (level % 2 == 1)
                Collections.reverse(list);
            listlist.add(list);
            currentLevel = nextLevel;
            level++;
        }
        return listlist;
    }
}
```