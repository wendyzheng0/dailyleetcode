#include <queue>
#include <climits>


/**
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

返回总和 最大 的那一层的层号 x。如果有多层的总和一样大，返回其中 最小 的层号 x。

按层遍历二叉树，计算每层的和，然后返回和最大的层号。
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int maxsum = INT_MIN, idx = 1, res = -1;
        queue<TreeNode*> layer;
        layer.push(root);
        while (layer.size() > 0) {
            int s = 0;
            int size = layer.size();
            for (int i = 0; i < size; i ++) {
                TreeNode* node = layer.front();
                layer.pop();
                s += node->val;
                if (node->left != NULL) {
                    layer.push(node->left);
                }
                if (node->right != NULL) {
                    layer.push(node->right);
                }
            }
            if (s > maxsum) {
                maxsum = s;
                res = idx;
            }
            idx++;
        }
        return res;
    }
};