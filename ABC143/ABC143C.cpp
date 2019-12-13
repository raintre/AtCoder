#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;
    
    int res = 0;
    for (int i = 0; i < N;) {
        int j = i;
        //同じ文字が連続している場合は添え字が増えていく
        while (j < N && S[j] == S[i]) ++j;
        ++res;
        i = j;
    }
    cout << res << endl;
}