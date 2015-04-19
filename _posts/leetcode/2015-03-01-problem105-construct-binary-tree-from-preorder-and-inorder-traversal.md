---
layout: post
title: LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/>***
<pre><code>/**
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 * 
 * Note: You may assume that duplicates do not exist in the tree.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (null == preorder || null == inorder) {
            return null;
        }

        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    private TreeNode buildTree(int[] preorder, int pStart, int pEnd,
            int[] inorder, int iStart, int iEnd) {
        if (iStart > iEnd) {
            return null;
        }

        int rootVal = preorder[pStart];
        TreeNode rootNode = new TreeNode(rootVal);
        int rootIndex = 0;
        while (rootIndex < iEnd - iStart + 1) {
            if (inorder[iStart + rootIndex] == rootVal) {
                break;
            }
            rootIndex++;
        }
        TreeNode leftNode = buildTree(preorder, pStart + 1, pStart + rootIndex, inorder, iStart, iStart + rootIndex - 1);
        TreeNode rightNode = buildTree(preorder, pStart + rootIndex + 1, pEnd, inorder, iStart + rootIndex + 1, iEnd);
        rootNode.left = leftNode;
        rootNode.right = rightNode;

        return rootNode;
    }
}
</code></pre>