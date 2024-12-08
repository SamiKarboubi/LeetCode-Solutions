/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sum(struct TreeNode* root){
    if(root==NULL){
        return 0;
    }
    return root->val+sum(root->left)+sum(root->right);
}
int findTilt(struct TreeNode* root) {
    if(root==NULL){
        return 0;
    }
    return abs(sum(root->right)-sum(root->left))+findTilt(root->left)+findTilt(root->right);
}
