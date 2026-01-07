#include <unordered_map>
#include <climits>
#include <cmath>


/**
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。
由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

第一遍遍历求整棵树的和并记录各节点为根的子树的和。第二遍遍历尝试分割每条边，计算分割后两棵子树的和的乘积，更新最大值。
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
    int MOD = 1000000007;
    unordered_map<TreeNode*, long long> map;
    long long total = 0;
public:
    long long calsubtree(TreeNode* node) {
        long long s = node->val;
        if (node->left) {
            s += this->calsubtree(node->left);
        }
        if (node->right) {
            s += this->calsubtree(node->right);
        }
        map[node] = s;
        return s;
    }

    long long trySplit(TreeNode* node) {
        long long ret = 0;
        if (node->left) {
            long long val = this->map[node->left];
            ret = val * (this->total - val);
            long long r = this->trySplit(node->left);
            if (r > ret) {
                ret = r;
            }
        }
        if (node->right) {
            long long val = this->map[node->right];
            long long r = val * (this->total - val);
            if (r > ret) {
                ret = r;
            }
            r = this->trySplit(node->right);
            if (r > ret) {
                ret = r;
            }
        }
        return ret;
    }

    int maxProduct(TreeNode* root) {
        this->total = this->calsubtree(root);
        return int(this->trySplit(root) % MOD);
    }
};