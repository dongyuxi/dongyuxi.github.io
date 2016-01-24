---
layout: post
title: LeetCode 021 - Merge Two Sorted Lists - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem021-merge-two-sorted-lists
---
***<https://leetcode.com/problems/merge-two-sorted-lists/>***
<!--more-->
```java
/**
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 * 
 * @author dongyuxi
 *
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (null == l1 && null == l2) {
            return null;
        }
        ListNode tempL1 = l1;
        ListNode tempL2 = l2;
        ListNode head = null;
        ListNode tempHead = null;
        while (null != tempL1 || null != tempL2) {
            int val = 0;
            if (null != tempL1 && null != tempL2) {
                int val1 = tempL1.val;
                int val2 = tempL2.val;
                if (val1 <= val2) {
                    val = val1;
                    tempL1 = tempL1.next;
                } else {
                    val = val2;
                    tempL2 = tempL2.next;
                }
            } else if (null != tempL1) {
                val = tempL1.val;
                tempL1 = tempL1.next;
            } else if (null != tempL2) {
                val = tempL2.val;
                tempL2 = tempL2.next;
            }
            ListNode newNode = new ListNode(val);
            if (null == head) {
                head = newNode;
                tempHead = head;
            } else {
                tempHead.next = newNode;
                tempHead = tempHead.next;
            }
        }
        return head;
    }
}
```