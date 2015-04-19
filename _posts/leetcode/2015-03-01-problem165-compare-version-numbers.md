---
layout: post
title: LeetCode 165 - Compare Version Numbers - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/compare-version-numbers/>***
<pre><code>/**
 * Compare two version numbers version1 and version2. If version1 > version2
 * return 1, if version1 < version2 return -1, otherwise return 0.
 * 
 * You may assume that the version strings are non-empty and contain only digits
 * and the . character. The . character does not represent a decimal point and
 * is used to separate number sequences. For instance, 2.5 is not
 * "two and a half" or "half way to version three", it is the fifth second-level
 * revision of the second first-level revision.
 * 
 * Here is an example of version numbers ordering:
 * 
 * 0.1 < 1.1 < 1.2 < 13.37
 * 
 * @author dongyuxi
 * 
 */
public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] verArr1 = version1.split("\\.");
        String[] verArr2 = version2.split("\\.");
        int index1 = 0;
        int index2 = 0;
        while (index1 < verArr1.length || index2 < verArr2.length) {
            int val1 = 0;
            int val2 = 0;
            if (index1 < verArr1.length) {
                val1 = Integer.parseInt(verArr1[index1++]);
            }
            if (index2 < verArr2.length) {
                val2 = Integer.parseInt(verArr2[index2++]);
            }
            if (val1 < val2) {
                return -1;
            }
            if (val1 > val2) {
                return 1;
            }
        }

        return 0;
    }
}
</code></pre>