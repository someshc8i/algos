#include <iostream>
using namespace std;
void print(int arr[], int n);

void print(int arr[], int n ) {
    for(int i=0; i < n; i++) {
        cout << arr[i];
    }
    cout << endl;
}

void leftRotateByOne(int arr[], int n) {
    int temp = arr[0];
    for(int i=0; i <n-1; i++) {
        arr[i] = arr[i+1];
    }
    arr[n-1] = temp;
}

void leftRotate (int arr[], int n, int d) {
    for (int i=0; i < d; i++) {
        leftRotateByOne(arr, n);
    }
}

int main() {
    int a[5] = {1,2,3,4,5};
    leftRotate(a, 5, 2);
    print(a, 5);
}
