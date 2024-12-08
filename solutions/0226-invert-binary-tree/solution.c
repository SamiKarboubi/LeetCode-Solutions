/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root) {
    if(root==NULL){
        return NULL;
    }
    struct TreeNode* c = root->right;
    root->right=root->left;
    root->left=c;
    invertTree(root->left);
    invertTree(root->right);
    return root;
}
