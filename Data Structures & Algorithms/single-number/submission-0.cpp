class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(auto c: nums){
            if (count(nums.begin() , nums.end(), c)==1) return c;
        }
        return 0;
    }
};
