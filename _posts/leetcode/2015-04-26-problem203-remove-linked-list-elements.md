---
layout: post
title: LeetCode 203 - Remove Linked List Elements - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/remove-linked-list-elements/>***
<pre><code>/**
 * Remove all elements from a linked list of integers that have value val.
 * 
 * Example
 * 
 * Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
 * 
 * Return: 1 --> 2 --> 3 --> 4 --> 5
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (null == head) {
            return head;
        }
        ListNode newHead = null;
        ListNode cur = null;
        ListNode temp = head;
        while (null != temp) {
            while (null != temp && val == temp.val) {
                temp = temp.next;
            }
            if (null == newHead) {
                newHead = temp;
                cur = newHead;
            } else {
                if (null != temp) {
                    cur.next = temp;
                    cur = cur.next;
                }
            }
            if (null != temp) {
                temp = temp.next;
            }
        }
        if (null != cur) {
            cur.next = null;
        }
        return newHead;
    }
}
</code></pre>