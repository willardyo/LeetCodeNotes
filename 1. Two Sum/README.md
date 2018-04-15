Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

此题类似找配对，找到a、b使得a+b=target。最容易想到的暴力搜索肯定可以，但时间复杂度为O(n^2)，会超时限，需要想一个时间复杂度为O(n)的算法实现。
既然是要找配对，那么key-value结构很适用，Java solution 用Hash表，Python solution用Dict，需要注意遍历过程中记录什么才是关键，正确的做法
是让key就是要找的b，让value记录a的Index，即结果需要的索引。
