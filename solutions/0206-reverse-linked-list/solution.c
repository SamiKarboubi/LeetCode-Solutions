/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev=NULL;
    struct ListNode* n=NULL;
    while(head)
    {
        n=head->next;
        head->next=prev;
        prev=head;
        head=n;
    }
    head=prev;
    return head;
}
