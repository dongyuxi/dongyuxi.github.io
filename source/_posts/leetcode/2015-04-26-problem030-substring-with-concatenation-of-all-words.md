---
layout: post
title: LeetCode 030 - Substring with Concatenation of All Words - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-04-26
permalink: problem030-substring-with-concatenation-of-all-words
---
***<https://leetcode.com/problems/substring-with-concatenation-of-all-words/>***
<!--more-->
```java
/**
 * You are given a string, s, and a list of words, words, that are all of the
 * same length. Find all starting indices of substring(s) in s that is a
 * concatenation of each word in words exactly once and without any intervening
 * characters.
 * 
 * For example, given: s: "barfoothefoobarman" words: ["foo", "bar"]
 * 
 * You should return the indices: [0,9]. (order does not matter).
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == s || 0 == s.length() || null == words || 0 == words.length) {
            return list;
        }
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (String word : words) {
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }
        int wordsNumber = words.length;
        int wordLength = words[0].length();
        for (int i = 0; i <= s.length() - wordsNumber * wordLength; i++) {
            Map<String, Integer> tempMap = new HashMap<String, Integer>(map);
            for (int j = i; j <= i + (wordsNumber - 1) * wordLength; j += wordLength) {
                String subword = s.substring(j, j + wordLength);
                if (tempMap.containsKey(subword)) {
                    if (tempMap.get(subword) == 1) {
                        tempMap.remove(subword);
                    } else {
                        tempMap.put(subword, tempMap.get(subword) - 1);
                    }
                } else {
                    break;
                }
            }
            if (0 == tempMap.size()) {
                list.add(i);
            }
        }
        return list;
    }
}
```