class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1);
        if (n==0) {return {0};}
        if (n==1) {return {0, 1};}
        dp[0] = 0;
        dp[1] = 1;
        int offset = 2;
        for (int i =2 ;i < n+1;i++){
            if (offset * 2 == i) offset = i ;
            dp[i] = 1+ dp[i-offset];
            cout << i<< " " << offset << endl; 
        }
        return dp;
    }
};
