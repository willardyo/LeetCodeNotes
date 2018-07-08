You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

本题难度为Medium，并不算难题，算法很简单，链表的数据类型也不难。思路就是建立一个新链表，然后把输入的两个链表从头往后依次处理，每两个相加，添加一个新节点到新链表后面，关键就是要处理下进位问题。另外最高位的进位问题要在最后特殊处理一下。
