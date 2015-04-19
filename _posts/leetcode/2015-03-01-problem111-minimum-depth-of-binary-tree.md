---
layout: post
title: LeetCode 111 - Minimum Depth of Binary Tree - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/minimum-depth-of-binary-tree/>***
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
    public int minDepth(TreeNode root) {
        if (null == root) {
            return 0;
        }

        if (null == root.left && null == root.right) {
            return 1;
        }
        if (null == root.left) {
            return minDepth(root.right) + 1;
        }
        if (null == root.right) {
            return minDepth(root.left) + 1;
        }
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
</code></pre>