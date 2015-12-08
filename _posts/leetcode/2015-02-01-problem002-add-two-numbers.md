---
layout: post
title: LeetCode 002 - Add Two Numbers - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/add-two-numbers/>***
<pre><code>/**
 * You are given two linked lists representing two non-negative numbers. The
 * digits are stored in reverse order and each of their nodes contain a single
 * digit. Add the two numbers and return it as a linked list.
 * 
 * @Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) 
 * @Output: 7 -> 0 -> 8
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = null;
        ListNode temp = null;
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        boolean add = false;
        while (null != temp1 || null != temp2) {
            int value = 0;
            if (null != temp1) {
                value += temp1.val;
                temp1 = temp1.next;
            }
            if (null != temp2) {
                value += temp2.val;
                temp2 = temp2.next;
            }
            if (add) {
                value += 1;
            }
            add = value >= 10 ? true : false;
            value = value % 10;
            ListNode newNode = new ListNode(value);
            if (null == result) {
                result = newNode;
                temp = newNode;
            } else {
                temp.next = newNode;
                temp = newNode;
            }
        }
        if (add) {
            temp.next = new ListNode(1);
        }
        return result;
    }
}
</code></pre>
