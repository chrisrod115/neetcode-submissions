class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length() - 1;
        while (l < r)
        {
            while (l < r && !alphaNum(s[l]))
            {
                l++;
            }
            while (l < r && !alphaNum(s[r]))
            {
                r--;
            }
            if (myToLower(s[l]) != myToLower(s[r]))
            {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    bool alphaNum(char c)
    {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }

    char myToLower(char c)
    {
        if (c >= 'A' && c <= 'Z')
        {
            return c += 32;
        }
        else
        {
            return c;
        }
    }
};
