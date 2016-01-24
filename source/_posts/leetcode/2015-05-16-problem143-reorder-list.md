---
layout: post
title: LeetCode 143 - Reorder List - 题解/Solution
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-05-16
permalink: problem143-reorder-list
---
***<https://leetcode.com/problems/reorder-list/>***
<!--more-->
```java
/**
 * Given a singly linked list L: L0->L1->…->Ln-1->Ln,
 * reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->…
 * 
 * You must do this in-place without altering the nodes' values.
 * 
 * For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode reorderList(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }

        // find the middle of list
        ListNode slowIndex = head;
        ListNode fastIndex = head.next;
        while (null != fastIndex && null != fastIndex.next) {
            slowIndex = slowIndex.next;
            fastIndex = fastIndex.next.next;
        }

        // reverse the second half of list
        slowIndex.next = reverseList(slowIndex.next);

        // reorder the first half and the second half
        ListNode firstHalf = head;
        ListNode secondHalf = slowIndex.next;
        slowIndex.next = null;
        while (null != secondHalf) {
            ListNode firstHalfNext = firstHalf.next;
            ListNode secondHalfNext = secondHalf.next;
            firstHalf.next = secondHalf;
            secondHalf.next = firstHalfNext;
            firstHalf = firstHalfNext;
            secondHalf = secondHalfNext;
        }

        return head;
    }

    private ListNode reverseList(ListNode head) {
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
```