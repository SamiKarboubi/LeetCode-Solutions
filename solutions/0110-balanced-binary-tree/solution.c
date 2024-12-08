/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int height(struct TreeNode* root)
{
    if(root==NULL){
        return 0;
    }
    int hauteurg=height(root->left);
    int hauteurd=height(root->right);
    if(hauteurd<=hauteurg) return hauteurg+1;
    return (hauteurg>hauteurd ? hauteurg : hauteurd)+1;
}
bool isBalanced(struct TreeNode* root) {
    if(root==NULL)
    {
        return true;
    }
    int hauteurg=height(root->left);
    int hauteurd=height(root->right);
    return abs(hauteurg-hauteurd)<=1 && isBalanced(root->left) && isBalanced(root->right);
    
}
