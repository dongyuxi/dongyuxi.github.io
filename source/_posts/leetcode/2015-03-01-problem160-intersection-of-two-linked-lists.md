---
layout: post
title: LeetCode 160 - Intersection of Two Linked Lists - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem160-intersection-of-two-linked-lists
---
***<https://leetcode.com/problems/intersection-of-two-linked-lists/>***
<!--more-->
```java
/**
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 * 
 * For example, the following two linked lists:
 * 
 * A:           a1 -> a2
 *                      c1 -> c2 -> c3
 * B:     b1 -> b2 -> b3
 * begin to intersect at node c1.
 * Notes:
 *   If the two linked lists have no intersection at all, return null.
 *   The linked lists must retain their original structure after the function returns.
 *   You may assume there are no cycles anywhere in the entire linked structure.
 *   Your code should preferably run in O(n) time and use only O(1) memory.
 *   
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (null == headA || null == headB) {
            return null;
        }

        int lenA = 0, lenB = 0;
        ListNode tempA = headA, tempB = headB;
        while (null != tempA) {
            lenA++;
            tempA = tempA.next;
        }
        while (null != tempB) {
            lenB++;
            tempB = tempB.next;
        }
        int lenDiff = Math.abs(lenA - lenB);
        tempA = headA; tempB = headB;
        if (lenA <= lenB) {
            while (lenDiff > 0) {
                tempB = tempB.next;
                lenDiff--;
            }
        } else {
            while (lenDiff > 0) {
                tempA = tempA.next;
                lenDiff--;
            }
        }

        while (null != tempA && null != tempB) {
            if (tempA == tempB) {
                break;
            }
            tempA = tempA.next;
            tempB = tempB.next;
        }

        if (null == tempA && null == tempB) {
            return null;
        }
        return tempA;
    }
}
```