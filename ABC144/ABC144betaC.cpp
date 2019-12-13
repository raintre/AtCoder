#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
  ll n; cin >> n;
  ll cnt = n;
  for (ll i = 1; i <= 1e6; ++i) {
    if (n % i == 0) {
      ll tmp = i + n / i - 2;
      if (tmp < cnt) cnt = tmp;
    }
  }
  cout << cnt << endl;
}
