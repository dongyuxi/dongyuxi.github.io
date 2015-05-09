---
layout: post
title: LeetCode 206 - Reverse Linked List - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/reverse-linked-list/>***
<pre><code>/**
 * Reverse a singly linked list.
 * 
 * Example
 * 
 * Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6
 * 
 * Return: 6 --> 5 --> 4 --> 3 --> 6 --> 2 --> 1
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        ListNode prev = head;
        ListNode cur = head.next;
        while (null != cur) {
            ListNode next = cur.next;
            cur.next = prev;
            if (prev == head) {
                prev.next = null;
            }
            prev = cur;
            cur = next;
        }
        return prev;
    }
}
</code></pre>
