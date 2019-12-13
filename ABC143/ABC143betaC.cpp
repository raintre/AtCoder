#include <bits/stdc++.h>
using namespace std;

int main() {
  //入力
  int n;
  cin >> n;
  string s;
  cin >> s;

  //stringの初期値はアルファベットと被らないように空文字にする
  char c = ' ';

  //文字列カウンタをゼロにセットする
  int res = 0;

  //全ての文字列を調べる
  for (char string_element : s) {
  //違う文字列に当たったらカウンタを更新
    if (string_element != c) {
      ++res;
    }
  //文字の種類を更新する
    c = string_element;
  }
  //結果を出力
  cout << res << endl;

  return 0;
}
