---
layout: post
title: LeetCode 155 - Min Stack - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/min-stack/>***
<pre><code>/**
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 * 
 * 
 * @author dongyuxi
 *
 */
class MinStack {
    private List<Integer> list = null;
    private List<Integer> min = null;

    public MinStack() {
        list = new ArrayList<Integer>();
        min = new ArrayList<Integer>();
    }

    public void push(int x) {
        list.add(x);
        if (0 == min.size() || x < min.get(min.size() - 1)) {
            min.add(x);
        } else {
            min.add(min.get(min.size() - 1));
        }
    }

    public void pop() {
        list.remove(list.size() - 1);
        min.remove(min.size() - 1);
    }

    public int top() {
        return list.get(list.size() - 1);
    }

    public int getMin() {
        return min.get(min.size() - 1);
    }
}
</code></pre>