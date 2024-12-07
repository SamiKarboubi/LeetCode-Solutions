/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if(!head || left == right){
        return head;
    }
    struct ListNode* prev = NULL;
    struct ListNode* current = head;
    for(int i=1; i<left;i++){
        prev=current;
        current=current->next;
    }
    struct ListNode* beforestart = prev;
    struct ListNode* start = current;
    struct ListNode* next = NULL;
    for(int i=0;i<=right -left;i++){
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    if(beforestart){
        beforestart->next=prev;
    }else{
        head=prev;
    }
    start->next=current;
    return head;
}
