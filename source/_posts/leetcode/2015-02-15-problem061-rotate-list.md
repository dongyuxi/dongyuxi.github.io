---
layout: post
title: LeetCode 061 - Rotate List - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem061-rotate-list
---
***<https://leetcode.com/problems/rotate-list/>***
<!--more-->
```java
/**
 * Given a list, rotate the list to the right by k places, where k is
 * non-negative.
 * 
 * For example: Given 1->2->3->4->5->NULL and k = 2, return 4->5->1->2->3->NULL.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int n) {
        if (null == head || 0 == n) {
            return head;
        }
        int length = 0;
        ListNode tmpHead = head;
        while (null != tmpHead) {
            length++;
            tmpHead = tmpHead.next;
        }
        if (n % length == 0) {
            return head;
        }
        n = n % length;
        ListNode fasterTmpHead = head;
        tmpHead = head;
        for (int i = 0; i < n; i++) {
            fasterTmpHead = fasterTmpHead.next;
        }
        while (null != fasterTmpHead.next) {
            tmpHead = tmpHead.next;
            fasterTmpHead = fasterTmpHead.next;
        }
        ListNode newHead = tmpHead.next;
        tmpHead.next = null;
        fasterTmpHead.next = head;

        return newHead;
    }
}
```