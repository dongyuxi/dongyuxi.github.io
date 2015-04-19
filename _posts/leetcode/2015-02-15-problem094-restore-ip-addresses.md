---
layout: post
title: LeetCode 093 - Restore IP Addresses - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/restore-ip-addresses/>***
<pre><code>/**
 * Given a string containing only digits, restore it by returning all possible
 * valid IP address combinations.
 * 
 * For example: Given "25525511135",
 * 
 * return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> list = new ArrayList<String>();
        if (null == s || 0 == s.length()) {
            return list;
        }

        StringBuilder sb = new StringBuilder();
        restoreIpAddresses(s, 0, 0, list, sb);
        return list;
    }

    private void restoreIpAddresses(String s, int index, int count,
            List<String> list, StringBuilder sb) {
        if (index > s.length() || count > 4) {
            return;
        }
        if (s.length() == index) {
            if (4 == count) {
                list.add(new String(sb.toString()));
                return;
            }
            return;
        }
        if (count > 0) {
            sb.append(".");
        }

        // 1 digit
        sb.append(s.charAt(index));
        restoreIpAddresses(s, index + 1, count + 1, list, sb);
        sb.deleteCharAt(sb.length() - 1);

        // 2 digits
        if (index < s.length() - 1 && '0' != s.charAt(index)) {
            sb.append(s.charAt(index)).append(s.charAt(index + 1));
            restoreIpAddresses(s, index + 2, count + 1, list, sb);
            sb.delete(sb.length() - 2, sb.length());
        }

        // 3 digits
        if (index < s.length() - 2 && '0' != s.charAt(index)) {
            int number = 100 * (s.charAt(index) - '0') + 10
                    * (s.charAt(index + 1) - '0') + s.charAt(index + 2) - '0';
            if (number <= 255) {
                sb.append(s.charAt(index)).append(s.charAt(index + 1))
                        .append(s.charAt(index + 2));
                restoreIpAddresses(s, index + 3, count + 1, list, sb);
                sb.delete(sb.length() - 3, sb.length());
            }
        }

        if (count > 0) {
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
</code></pre>