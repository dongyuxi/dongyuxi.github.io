---
layout: post
title: LeetCode 094 - Binary Tree Inorder Traversal - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/binary-tree-inorder-traversal/>***
<pre><code>/**
 * Given a binary tree, return the inorder traversal of its nodes' values.
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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) {
            return list;
        }

        inorderTraversal(root, list);

        return list;
    }

    private void inorderTraversal(TreeNode root, List<Integer> list) {
        if (null == root) {
            return;
        }
        inorderTraversal(root.left, list);
        list.add(root.val);
        inorderTraversal(root.right, list);
    }
}
</code></pre>
