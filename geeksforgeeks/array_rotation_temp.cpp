#include <iostream>
using namespace std;
void print(int arr[], int n);

void rotate_arr(int arr[], int n, int d) {
    int temp[d];
    for (int i=0; i < d; i++) {
        temp[i] = arr[i];
    }
    for (int i=0; i < n-d; i++) {
        arr[i] = arr[i + d];
    }
    for (int i=n-d; i < n ; i++){
        arr[i] = temp[i-n+d];
    }
}

void print(int arr[], int n ) {
    for(int i=0; i < n; i++) {
        cout << arr[i];
    }
    cout << endl;
}

int main() {
    int a[7] = {1,2,3,4,5,6,7};
    rotate_arr(a, 7, 6);
    print(a, 7);
    return 0;
}
