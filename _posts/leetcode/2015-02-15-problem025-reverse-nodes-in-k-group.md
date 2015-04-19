---
layout: post
title: LeetCode 025 - Reverse Nodes in k-Group - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/reverse-nodes-in-k-group/>***
<pre><code>/**
 * Given a linked list, reverse the nodes of a linked list k at a time and
 * return its modified list.
 * 
 * If the number of nodes is not a multiple of k then left-out nodes in the end
 * should remain as it is.
 * 
 * You may not alter the values in the nodes, only nodes itself may be changed.
 * 
 * Only constant memory is allowed.
 * 
 * For example, Given this linked list: 1->2->3->4->5
 * 
 * For k = 2, you should return: 2->1->4->3->5
 * 
 * For k = 3, you should return: 3->2->1->4->5
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (null == head || null == head.next || 1 == k) {
            return head;
        }

        ListNode tmpHead = new ListNode(-1);
        tmpHead.next = head;
        ListNode preNode = tmpHead;
        ListNode curNode = head;
        ListNode nextNode = curNode;
        while (null != nextNode) {
            int count = k - 1;
            while (count > 0 && null != nextNode.next) {
                nextNode = nextNode.next;
                count--;
            }
            if (count == 0) {
                if (tmpHead.next == head) {
                    tmpHead.next = nextNode;
                }
                preNode.next = nextNode;
                preNode = curNode;
                ListNode nextnext = nextNode.next;
                nextNode = curNode.next;
                curNode.next = nextnext;
                while (nextNode != nextnext) {
                    ListNode tempNext = nextNode.next;
                    nextNode.next = curNode;
                    curNode = nextNode;
                    nextNode = tempNext;
                }
                curNode = nextnext;
            } else {
                break;
            }
        }

        return tmpHead.next;
    }
}
</code></pre>