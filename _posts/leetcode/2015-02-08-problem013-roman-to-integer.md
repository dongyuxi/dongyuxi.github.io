---
layout: post
title: LeetCode 013 - Integer to Roman - 题解/Solution
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/roman-to-integer/>***
<pre><code>/**
 * Given a roman numeral, convert it to an integer.
 * 
 * Input is guaranteed to be within the range from 1 to 3999.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    private final static Map<Character, Integer> MAP = new HashMap<Character, Integer>();
    static {
        MAP.put('I', 1);
        MAP.put('V', 5);
        MAP.put('X', 10);
        MAP.put('L', 50);
        MAP.put('C', 100);
        MAP.put('D', 500);
        MAP.put('M', 1000);
    }

    public int romanToInt(String s) {
        int sum = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (i == s.length() - 1) {
                sum += MAP.get(s.charAt(i));
            } else {
                if (MAP.get(s.charAt(i)) < MAP.get(s.charAt(i + 1))) {
                    sum -= MAP.get(s.charAt(i));
                } else {
                    sum += MAP.get(s.charAt(i));
                }
            }
        }
        return sum;
    }
}
</code></pre>
