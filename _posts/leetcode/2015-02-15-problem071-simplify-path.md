---
layout: post
title: LeetCode 071 - Simplify Path - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/simplify-path/>***
<pre><code>/**
 * Given an absolute path for a file (Unix-style), simplify it.
 * 
 * For example,
 * path = "/home/", => "/home"
 * path = "/a/./b/../../c/", => "/c"
 * 
 * Corner Cases: Did you consider the case where path = "/../"? In this case,
 * you should return "/". Another corner case is the path might contain multiple
 * slashes '/' together, such as "/home//foo/". In this case, you should ignore
 * redundant slashes and return "/home/foo".
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String simplifyPath(String path) {
        if (null == path) {
            return "/";
        }

        List<String> dirList = new ArrayList<String>();
        int depth = 0;
        String[] dirs = path.split("\\/");
        for (int i = 0; i < dirs.length; i++) {
            if ("".equals(dirs[i]) || ".".equals(dirs[i])) {
                continue;
            }
            if ("..".equals(dirs[i])) {
                if (depth > 0 && depth <= dirList.size()) {
                    dirList.remove(depth - 1);
                    depth--;
                }
            } else {
                if (depth >= 0) {
                    dirList.add(dirs[i]);
                }
                depth++;
            }
        }

        if (depth <= 0) {
            return "/";
        }

        StringBuilder sb = new StringBuilder();
        for (String dir : dirList) {
            sb.append("/").append(dir);
        }

        return sb.toString();
    }
}
</code></pre>
