---
layout: post
title: LeetCode 110 - Balanced Binary Tree - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem110-balanced-binary-tree
---
***<https://leetcode.com/problems/balanced-binary-tree/>***
<!--more-->
```java
/**
 * Given a binary tree, determine if it is height-balanced.
 * 
 * For this problem, a height-balanced binary tree is defined as a binary tree
 * in which the depth of the two subtrees of every node never differ by more
 * than 1.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    private boolean balanced = true;

    public boolean isBalanced(TreeNode root) {
        if (null == root) {
            return true;
        }

        int depth = checkBalancedUsingHeihg(root);

        return (depth != -1) ? true : false;
    }

    private int checkBalancedUsingHeihg(TreeNode root) {
        if (!balanced) {
            return -1;
        }

        if (null == root) {
            return 0;
        }

        int leftDepth = checkBalancedUsingHeihg(root.left);
        int rightDepth = checkBalancedUsingHeihg(root.right);
        if (leftDepth == -1 || rightDepth == -1 || Math.abs(leftDepth - rightDepth) > 1) {
            return -1;
        }
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```