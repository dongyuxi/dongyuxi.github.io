---
layout: post
title: LeetCode 145 - Binary Tree Postorder Traversal - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem145-binary-tree-postorder-traversal
---
***<https://leetcode.com/problems/binary-tree-postorder-traversal/>***
<!--more-->
```java
/**
 * Given a binary tree, return the postorder traversal of its nodes' values.
 * 
 * For example: Given binary tree {1,#,2,3},
 * 
 *   1 
 *    \
 *     2 
 *    /
 *   3
 * 
 * return [1,3,2].
 * 
 * Note: Recursive solution is trivial, could you do it iteratively?
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) {
            return list;
        }

        postorderTraversal(root, list);

        return list;
    }

    private void postorderTraversal(TreeNode root, List<Integer> list) {
        if (null == root) {
            return;
        }
        postorderTraversal(root.left, list);
        postorderTraversal(root.right, list);
        list.add(root.val);
    }
}
```