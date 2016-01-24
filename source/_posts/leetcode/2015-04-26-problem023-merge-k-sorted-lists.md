---
layout: post
title: LeetCode 023 - Merge k Sorted Lists - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-04-26
permalink: problem023-merge-k-sorted-lists
---
***<https://leetcode.com/problems/merge-k-sorted-lists/>***
<!--more-->
```java
/**
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (null == lists || 0 == lists.length) {
            return null;
        }
        return mergeKLists(lists, 0, lists.length - 1);
    }

    private ListNode mergeKLists(ListNode[] lists, int start, int end) {
        if (start < end) {
            int mid = start + (end - start) / 2;
            ListNode firstList = mergeKLists(lists, start, mid);
            ListNode secondList = mergeKLists(lists, mid + 1, end);
            return merge2Lists(firstList, secondList);
        }
        return lists[start];
    }

    private ListNode merge2Lists(ListNode firstList, ListNode secondList) {
        ListNode dummyHead = new ListNode(0);
        ListNode cur = dummyHead;
        while (null != firstList && null != secondList) {
            if (firstList.val < secondList.val) {
                cur.next = firstList;
                firstList = firstList.next;
            } else {
                cur.next = secondList;
                secondList = secondList.next;
            }
            cur = cur.next;
        }
        if (null != firstList) {
            cur.next = firstList;
        } else {
            cur.next = secondList;
        }
        return dummyHead.next;
    }
}
```