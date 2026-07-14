// Last updated: 7/14/2026, 2:17:11 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";

        // Take first word as reference
        String first = strs[0];

        for (int i = 0; i < first.length(); i++) {
            char c = first.charAt(i);

            // Compare this char with all other words
            for (int j = 1; j < strs.length; j++) {
                // If index is out of range OR char does not match
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return first.substring(0, i);
                }
            }
        }

        return first; // Whole first word is common
    }
}

