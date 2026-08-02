/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        // let is mutable
        // const is immutable (cannot redeclare)

        let prv = null;
        let cur = head;
        while (cur) {
            let tmp = cur.next;
            cur.next = prv;
            prv = cur;
            cur = tmp;
        }
        return prv;
    }
}
