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
        let prv = null;
        let cur = head;
        while (cur) {
            const tmp = cur.next;
            cur.next = prv;
            prv = cur;
            cur = tmp;
        }
        return prv;
    }
}
