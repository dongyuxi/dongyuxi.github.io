---
layout: post
title: LeetCode 101 - Symmetric Tree - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/symmetric-tree/>***
<pre><code>/**
 * Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
 * For example, this binary tree is symmetric:
 * 
 *       1
 *      / \
 *     2   2
 *    / \ / \
 *   3  4 4  3
 * But the following is not:
 *       1
 *      / \
 *     2   2
 *      \   \
 *      3    3
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (null == root) {
            return true;
        }

        return recursiveIsSymmetric(root.left, root.right);
    }

    private boolean recursiveIsSymmetric(TreeNode left, TreeNode right) {
        if (null == left && null == right) {
            return true;
        }
        if (null == left || null == right) {
            return false;
        }
        boolean leftLeftRightRight = recursiveIsSymmetric(left.left, right.right);
        boolean leftRightRightLeft = recursiveIsSymmetric(left.right, right.left);
        if (leftLeftRightRight && leftRightRightLeft && left.val == right.val) {
            return true;
        }

        return false;
    }
}
</code></pre>
