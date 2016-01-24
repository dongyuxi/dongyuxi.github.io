---
layout: post
title: LeetCode 127 - Word Ladder - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem127-word-ladder
---
***<https://leetcode.com/problems/word-ladder/>***
<!--more-->
```java
/**
 * Given two words (start and end), and a dictionary, find the length of
 * shortest transformation sequence from start to end, such that:
 * 
 * Only one letter can be changed at a time Each intermediate word must exist in
 * the dictionary
 * 
 * For example,
 * 
 * Given: start = "hit" end = "cog" dict = ["hot","dot","dog","lot","log"]
 * 
 * As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * return its length 5.
 * 
 * Note:
 * 
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int ladderLength(String start, String end, Set<String> dict) {
        if (null == start || null == end || null == dict) {
            return 0;
        }

        LinkedList<String> queue = new LinkedList<String>();
        LinkedList<Integer> distanceQueue = new LinkedList<Integer>();
        queue.add(start);
        distanceQueue.add(1);
        dict.remove(start);
        while (!queue.isEmpty()) {
            String first = queue.pop();
            Integer distance = distanceQueue.pop();
            for (int i = 0; i < first.length(); i++) {
                char[] charArray = first.toCharArray();
                for (char j = 'a'; j <= 'z'; j++) {
                    charArray[i] = j;
                    String candidate = new String(charArray);
                    if (candidate.equals(end)) {
                        return distance + 1;
                    }
                    if (dict.contains(candidate)) {
                        queue.add(candidate);
                        distanceQueue.add(distance + 1);
                        dict.remove(candidate);
                    }
                }
            }
        }

        return 0;
    }
}
```