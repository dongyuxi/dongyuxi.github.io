---
layout: post
title: LeetCode 142 - Linked List Cycle II - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/linked-list-cycle-ii/>***
<pre><code>/**
 * Given a linked list, determine if it has a cycle in it.
 * 
 * Follow up: Can you solve it without using extra space?
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (null == head || null == head.next) {
            return null;
        }

        ListNode stepOneHead = head.next;
        ListNode stepTwoHead = head.next.next;
        while (null != stepOneHead && null != stepTwoHead) {
            if (stepOneHead == stepTwoHead) {
                break;
            }
            stepOneHead = stepOneHead.next;
            if (null == stepTwoHead.next) {
                return null;
            }
            stepTwoHead = stepTwoHead.next.next;
        }

        if (null == stepTwoHead || null == stepTwoHead.next) {
            return null;
        }

        stepTwoHead = head;
        while (stepOneHead != stepTwoHead) {
            stepOneHead = stepOneHead.next;
            stepTwoHead = stepTwoHead.next;
        }

        return stepOneHead;
    }
}
</code></pre>
