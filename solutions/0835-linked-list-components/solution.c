/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int numComponents(struct ListNode* head, int* nums, int numsSize)
{
    bool hashtable[10000]={false};
    for(int i=0;i<numsSize;i++){
        hashtable[nums[i]]=true;
    }
    int count = 0;
    struct ListNode* current=head;
    bool incomp = false;
    while(current!=NULL){
        if(hashtable[current->val]){
            if(!incomp){
                count++;
                incomp=true;
            }
       }else{
            incomp=false;
       }
       current=current->next;
    }
    return count;
}
