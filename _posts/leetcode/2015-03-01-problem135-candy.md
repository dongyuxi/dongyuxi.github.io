---
layout: post
title: LeetCode 135 - Candy - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/candy/>***
<pre><code>/**
 * There are N children standing in a line. Each child is assigned a rating
 * value.
 * 
 * You are giving candies to these children subjected to the following
 * requirements:
 * 
 * Each child must have at least one candy. Children with a higher rating get
 * more candies than their neighbors.
 * 
 * What is the minimum candies you must give?
 * 
 * @author dongyuxi
 * 
 */
public class Solution {
    public int candy(int[] ratings) {
        if (null == ratings || 0 == ratings.length) {
            return 0;
        }

        int candy = 1;
        int upMax = 1;
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                int curCandy = 1;
                while (i < ratings.length && ratings[i] > ratings[i - 1]) {
                    curCandy++;
                    candy += curCandy;
                    i++;
                }
                i--;
                upMax = curCandy;
            } else if (ratings[i] == ratings[i - 1]) {
                candy++;
                upMax = 1;
            } else {
                int curCandy = 1;
                while (i < ratings.length && ratings[i] < ratings[i - 1]) {
                    candy += curCandy;
                    curCandy++;
                    i++;
                }
                i--;
                if (curCandy > upMax) {
                    candy = candy - upMax + curCandy;
                }
            }
        }

        return candy;
    }
}
</code></pre>