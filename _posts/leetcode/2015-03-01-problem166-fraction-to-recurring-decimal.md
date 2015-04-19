---
layout: post
title: LeetCode 166 - Fraction to Recurring Decimal - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/fraction-to-recurring-decimal/>***
<pre><code>/**
 * Given two integers representing the numerator and denominator of a fraction,
 * return the fraction in string format.
 * 
 * If the fractional part is repeating, enclose the repeating part in
 * parentheses.
 * 
 * For example,
 * 
 * Given numerator = 1, denominator = 2, return "0.5".
 * Given numerator = 2, denominator = 1, return "2".
 * Given numerator = 2, denominator = 3, return "0.(6)".
 * 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        long numeratorLong = Math.abs((long)numerator);
        long denominatorLong = Math.abs((long)denominator);
        StringBuilder sb = new StringBuilder();
        if ((numerator < 0 && denominator > 0) || (numerator > 0 && denominator < 0)) {
            sb.append("-");
        }
        sb.append(numeratorLong / denominatorLong);
        long remaining = numeratorLong % denominatorLong;
        if (0 != remaining) {
            sb.append(".");
            Map<Long, Integer> map = new HashMap<Long, Integer>();
            while (0 != remaining) {
                if (map.containsKey(remaining)) {
                    sb.insert(map.get(remaining), "(");
                    sb.append(")");
                    break;
                }
                map.put(remaining, sb.length());
                remaining *= 10;
                sb.append(remaining / denominatorLong);
                remaining %= denominatorLong;
            }
        }

        return sb.toString();
    }
}
</code></pre>