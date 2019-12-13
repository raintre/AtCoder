#include <bits/stdc++.h>
using namespace std;

int main() {
//input
  int n;
  cin >> n;
  vector<int> arr(n);
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }
//arr 昇順
  sort(arr.begin(), arr.end());
//カウンタ0初期化
  int res = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      int min_k = distance(arr.begin(), lower_bound(arr.begin(), arr.end(), arr[j] - arr[i] + 1));
      int max_k = distance(arr.begin(), lower_bound(arr.begin(), arr.end(), arr[i] + arr[j]));
      res += max(0, max_k - max(j + 1, min_k));
    }
  }
  cout << res << endl;
}
