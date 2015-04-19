---
layout: post
title: LeetCode 109 - Convert Sorted List to Binary Search Tree - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/>***
<pre><code>/**
 * Given an array where elements are sorted in ascending order, convert it to a
 * height balanced BST.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (null == head) {
            return null;
        }

        int length = 0;
        ListNode tempHead = head;
        while (null != tempHead) {
            length++;
            tempHead = tempHead.next;
        }

        return sortedListToBST(head, length);
    }

    private TreeNode sortedListToBST(ListNode head , int length) {
        if (length <= 0 || null == head) {
            return null;
        }

        ListNode temp = head;
        for (int i = 0; i < length / 2; i++) {
            temp = temp.next;
        }
        TreeNode root = new TreeNode(temp.val);
        TreeNode left = sortedListToBST(head, length / 2);
        TreeNode right = sortedListToBST(temp.next, length - length / 2 - 1);
        root.left = left;
        root.right = right;

        return root;
    }
}
</code></pre>