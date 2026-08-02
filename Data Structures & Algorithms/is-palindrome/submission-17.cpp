class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length() - 1;
        while (l < r)
        {
            while ((l < r) && !(isAlnum(s[l])))
            {
                l++;
            }
            while ((l < r) && !(isAlnum(s[r])))
            {
                r--;
            }

            if (toLower(s[l]) == toLower(s[r]))
            {
                l++;
                r--;
            }
            else
            {
                return false;
            }
        }
        return true;
    }

    bool isAlnum(char c)
    {
        return(
            c >= 'A' && c <= 'Z' ||
            c >= 'a' && c <= 'z' ||
            c >= '0' && c <= '9'
            );
    }
    char toLower(char c)
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
