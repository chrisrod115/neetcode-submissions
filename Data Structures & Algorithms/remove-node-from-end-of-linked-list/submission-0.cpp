/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 /*
 head = [1,2,3,4], n = 2
             ^
        1 -> 2 -> 3 -> 4
                  ^    
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int counter = 0;
        ListNode* len = head;
        while (len) {
            counter++;
            len = len->next;
        }

        int remove_pos = counter - n;

        ListNode* remove = head;
        
        if (remove_pos == 0) {
            return head->next;
        }

        for (int i = 0; i < remove_pos; i++) {
            if (i == remove_pos - 1) {
                remove->next = remove->next->next;
            }
            remove = remove->next;
        }
        return head;
    }
};
