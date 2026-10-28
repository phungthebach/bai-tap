#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a[n+1];
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	int mi=a[1],kq=0;
	for(int i=2;i<=n;i++){
		if (mi>=a[i]){
			mi=a[i];
		}
		else kq=max(kq,a[i]-mi);
	}
	cout<<kq;
}