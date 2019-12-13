#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() 
{
    //input
    int n;
    ll k;
    cin >> n >> k;
    vector<int> a(n);
    vector<int> f(n);
    rep(i, n) cin >> a[i];
    rep(i, n) cin >> f[i];

    //a -> ascending order
    sort(a.begin(), a.end());
    //f -> descending order
    sort(f.rbegin(), f.rend());

    ll left = -1;
    ll right = 1e12;

    //2-minute search
    while (1 < right - left)
    {
        ll mid = (left + right) / 2;
        bool ok = [&] 
        {
            ll Difference = 0;
            rep(i, n) 
            {
                Difference += max(0ll, a[i] - mid / f[i]);
            }
            return Difference <= k;
        }();
        if (ok) right = mid; else left = mid;   
    }

    //output
    cout << right << endl;
    return 0;
}