---
layout: post
title: LeetCode 024 - Swap Nodes in Pairs - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem024-swap-nodes-in-pairs
---
***<https://leetcode.com/problems/swap-nodes-in-pairs/>***
<!--more-->
```java
/**
 * Given a linked list, swap every two adjacent nodes and return its head.
 * 
 * For example, Given 1->2->3->4, you should return the list as 2->1->4->3.
 * 
 * Your algorithm should use only constant space. You may not modify the values
 * in the list, only nodes itself can be changed.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }

        ListNode retHead = head.next;
        ListNode index = head;
        ListNode preNode = null;
        while (null != index && null != index.next) {
            ListNode temp1 = index;
            ListNode temp2 = index.next;
            index = index.next.next;
            temp1.next = temp2.next;
            temp2.next = temp1;
            if (null != preNode) {
                preNode.next = temp2;
            }
            preNode = temp1;
        }

        return retHead;
    }
}
```