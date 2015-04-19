---
layout: post
title: LeetCode 083 - Remove Duplicates from Sorted List - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/remove-duplicates-from-sorted-list/>***
<pre><code>/**
 * Given a sorted linked list, delete all nodes that have duplicate numbers,
 * leaving only distinct numbers from the original list.
 * 
 * For example, Given 1->2->3->3->4->4->5, return 1->2->5.
 * Given 1->1->1->2->3, return 2->3.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (null == head) {
            return null;
        }

        ListNode fakeHead = new ListNode(-1);
        fakeHead.next = null;
        ListNode prevHead = fakeHead;
        ListNode indexHead = head;
        ListNode nextHead = indexHead.next;
        int val = indexHead.val;
        boolean dup = false;
        while (null != indexHead) {
            if (null != nextHead) {
                if (val == nextHead.val) {
                    dup = true;
                    while (null != nextHead && nextHead.val == val) {
                        nextHead = nextHead.next;
                    }
                }
            }

            if (!dup) {
                prevHead.next = indexHead;
                prevHead = indexHead;
                prevHead.next = null;
            }
            indexHead = nextHead;
            if (null != nextHead) {
                val = nextHead.val;
                dup = false;
                nextHead = nextHead.next;
            }
        }

        return fakeHead.next;
    }
}
</code></pre>