class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        string ans = "";
        int  c_in;
        c_in = 0;
        for(int i =0 ; i< max(a.length(), b.length()) ; i++){
            int at = i < a.length() ? a[i] - '0' : 0;
            int bt =  i < b.length() ? b[i] - '0' : 0;
            char s = at +  bt + c_in;
            ans+= ((s%2) + '0');
            c_in = s/2;
        }
        if (c_in) ans += '1';
        reverse(ans.begin(), ans.end());
        cout << ans;
        return ans;
    }
};