---
layout: post
title: LeetCode 204 - Count Primes - 题解/Solution
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/count-primes/>***
<pre><code>/**
 * Count the number of prime numbers less than a non-negative number, n
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int countPrimes(int n) {
        if (n <= 2) {
            return 0;
        }
        boolean[] prime = new boolean[n];
        for (int i = 2; i * i < n; i++) {
            if (!prime[i]) {
                for (int j = i; i * j < n; j++) {
                    prime[i * j] = true;
                }
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (!prime[i]) {
                count++;
            }
        }
        return count;
    }
}
</code></pre>
