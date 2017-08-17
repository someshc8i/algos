
#include <iostream>
using namespace std;

void printArray(int arr[], int n)
{
    for(int i=0; i < n; i++) {
        cout << arr[i];
    }
    cout << endl;
}

void reverseArray(int arr[], int s, int e) {
    int temp;
    while (s < e)
    {
        temp = arr[s];
        arr[s] = arr[e];
        arr[e] = temp;
        s++;
        e--;
    }
}

void leftRotate (int arr[], int n, int d) {
    reverseArray(arr, 0, d-1);
    printArray(arr, n);
    reverseArray(arr, d, n-1);
    printArray(arr, n);
    reverseArray(arr, 0, n-1);
    printArray(arr, n);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
    int d = 2;
    leftRotate(arr, n, d);
    return 0;
}
