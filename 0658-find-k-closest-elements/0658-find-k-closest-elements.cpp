class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0;
        int right = size(arr) - 1;
        while ((right - left + 1) > k){
            if (abs(arr[left] - x) > abs(arr[right] - x)){
                left = left + 1;
            }
            else{
                right = right - 1;
            }
        }
        return vector<int>(arr.begin() + left, arr.begin() + right + 1);
    }
};