---
layout: post
title: LeetCode 104 - Maximum Depth of Binary Tree - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/maximum-depth-of-binary-tree/>***
<pre><code>/**
 * Given a binary tree, find its maximum depth.
 * 
 * The maximum depth is the number of nodes along the longest path from the root
 * node down to the farthest leaf node.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        if (null == root) {
            return 0;
        }

        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
</code></pre>