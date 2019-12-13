#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll n;
    cin >> n;
    //ansはでかい数で初期化
    ll ans = 1e18;
    for(ll i = 1; i*i <= n; i++) {
        //割り切れた場合のみ通過
        if(n % i != 0) continue;
        ll j = n/i;
        //最小値を探索し続ける
        ans = min(ans, i + j - 2);
    }
    cout << ans << endl;
    return 0;
}