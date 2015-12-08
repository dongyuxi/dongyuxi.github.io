---
layout: post
title: LeetCode 057 - Insert Interval - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/insert-interval/>***
<pre><code>/**
 * Given a set of non-overlapping intervals, insert a new interval into the
 * intervals (merge if necessary).
 * 
 * You may assume that the intervals were initially sorted according to their
 * start times.
 * 
 * Example 1: Given intervals [1,3],[6,9], insert and merge [2,5] in as
 * [1,5],[6,9].
 * 
 * Example 2: Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in
 * as [1,2],[3,10],[12,16].
 * 
 * This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new ArrayList<Interval>();
        if (null == intervals || 0 == intervals.size()) {
            result.add(newInterval);
            return result;
        }

        Collections.sort(intervals, new Comparator<Interval>() {
            @Override
            public int compare(Interval o1, Interval o2) {
                if (o1.start != o2.start) {
                    return o1.start - o2.start;
                }
                return o1.end - o2.end;
            }
        });

        boolean merged = false;
        for (int i = 0; i < intervals.size(); i++) {
            Interval interval = intervals.get(i);
            if (!merged && newInterval.start <= interval.end) {
                if (newInterval.end < interval.start) {
                    result.add(newInterval);
                } else {
                    int start = Math.min(interval.start, newInterval.start);
                    int end = Math.max(interval.end, newInterval.end);;
                    while (i < intervals.size()) {
                        if (newInterval.end >= intervals.get(i).start) {
                            end = Math.max(end, intervals.get(i).end);
                            i++;
                        } else {
                            break;
                        }
                    }
                    
                    Interval mergedInterval = new Interval(start, end);
                    result.add(mergedInterval);
                }
                merged = true;
                i--;
            } else {
                result.add(interval);
            }
        }
        if (!merged) {
            result.add(newInterval);
        }

        return result;
    }
}
</code></pre>
