---
layout: post
title: LeetCode 141 - Linked List Cycle - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/linked-list-cycle/>***
<pre><code>/**
 * Given a linked list, determine if it has a cycle in it.
 * 
 * Follow up: Can you solve it without using extra space?
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (null == head || null == head.next) {
            return false;
        }

        ListNode stepOneHead = head.next;
        ListNode stepTwoHead = head.next.next;
        while (null != stepOneHead && null != stepTwoHead) {
            if (stepOneHead == stepTwoHead) {
                return true;
            }
            stepOneHead = stepOneHead.next;
            if (null == stepTwoHead.next) {
                return false;
            }
            stepTwoHead = stepTwoHead.next.next;
        }

        return false;
    }
}
</code></pre>