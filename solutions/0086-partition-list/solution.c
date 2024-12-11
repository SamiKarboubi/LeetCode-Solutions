/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode *lesshead=NULL,*lesstail=NULL;
    struct ListNode *greaterhead=NULL,*greatertail=NULL;
    while(head){
        if(head->val<x){
            if(lesshead==NULL){
                lesshead=lesstail=head;
            }else{
                lesstail->next=head;
                lesstail=lesstail->next;
            }
        }
        else{
            if(greaterhead==NULL){
                greaterhead=greatertail=head;
            }
            else{
                greatertail->next=head;
                greatertail=greatertail->next;
            }
        }
        head=head->next;
    }
    
    if (greatertail) greatertail->next=NULL;
    if (lesstail) lesstail->next=greaterhead;
    return lesshead ? lesshead : greaterhead ;
}
