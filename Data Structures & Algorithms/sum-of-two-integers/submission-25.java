class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            int withoutCarry = a ^ b;
            a = withoutCarry;
            b = carry;
        }

        return a;
    }
}
