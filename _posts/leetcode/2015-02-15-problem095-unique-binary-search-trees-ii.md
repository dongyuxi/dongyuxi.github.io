---
layout: post
title: LeetCode 095 - Unique Binary Search Trees II - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/unique-binary-search-trees-ii/>***
<pre><code>/**
 * Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 * For example,
 * Given n = 3, there are a total of 5 unique BST's.
 * 
 *  1         3     3      2      1
 *   \       /     /      / \      \
 *    3     2     1      1   3      2
 *   /     /       \                 \
 *  2     1         2                 3
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ArrayList<TreeNode> generateTree(int start, int end) {
        ArrayList<TreeNode> result = new ArrayList<TreeNode>();
        if (start > end) {
            result.add(null);
            return result;
        }
        ArrayList<TreeNode> leftTree = new ArrayList<TreeNode>();
        ArrayList<TreeNode> rightTree = new ArrayList<TreeNode>();
        for (int i = start; i <= end; i++) {
            leftTree = generateTree(start, i - 1);
            rightTree = generateTree(i + 1, end);
            for (int j = 0; j < leftTree.size(); j++) {
                for (int k = 0; k < rightTree.size(); k++) {
                    TreeNode root = new TreeNode(i + 1);
                    root.left = leftTree.get(j);
                    root.right = rightTree.get(k);
                    result.add(root);
                }
            }
        }
        return result;
    }

    public ArrayList<TreeNode> generateTrees(int n) {
        return generateTree(0, n - 1);
    }
}
</code></pre>