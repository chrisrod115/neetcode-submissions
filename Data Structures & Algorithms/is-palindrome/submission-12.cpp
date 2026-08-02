
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length() - 1;
        while (l < r)
        {
            while ((l < r) && !isalnum(s[l]))
            {
                l += 1;
            }
            while ((l < r) && !isalnum(s[r]))
            {
                r -= 1;
            }
            if (tolower(s[l]) != tolower(s[r]))
            {
                return false;
            }
            l++;
            r--;
                        
        }
        return true;
    }
    bool isalnum(char c)
    {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
};
