---
layout: post
title: LeetCode 049 - Anagrams - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem049-anagrams
---
***<https://leetcode.com/problems/anagrams/>***
<!--more-->
```java
/**
 * Given an array of strings, return all groups of strings that are anagrams.
 * 
 * Note: All inputs will be in lower-case.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<String> anagrams(String[] strs) {
        List<String> list = new ArrayList<String>();
        if (null == strs || 0 == strs.length) {
            return list;
        }

        Map<String, String> map = new HashMap<String, String>();
        Map<String, Boolean> first = new HashMap<String, Boolean>();
        for (int i = 0; i < strs.length; i++) {
            char[] array = strs[i].toCharArray();
            Arrays.sort(array);
            String sortedString = String.valueOf(array);
            if (map.containsKey(sortedString)) {
                if (first.get(sortedString)) {
                    list.add(map.get(sortedString));
                    first.put(sortedString, false);
                }
                list.add(strs[i]);
            } else {
                map.put(sortedString, strs[i]);
                first.put(sortedString, true);
            }
        }
        return list;
    }
}
```