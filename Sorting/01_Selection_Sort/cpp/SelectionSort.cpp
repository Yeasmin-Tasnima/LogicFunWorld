#include<iostream>
using namespace std;

void selectionSort(int arr[], int n) {
	for (int i = 0; i < n - 1; i++) {
		int imin = i;
		for (int j = i + 1; j < n; j++) {
			if (arr[j] < arr[imin]) {
				imin = j;
			}
		}
		int temp = arr[imin];
		arr[imin] = arr[i];
		arr[i] = temp;
	}
}


int main() {
	int arr[] = { 2, 7, 4, 1, 5, 3 };
	int sizeOfArray = sizeof(arr) / sizeof(int);

	cout << "unsorted array: ";
	for (int i = 0; i < sizeOfArray; i++) {
		cout << arr[i] << " ";
	}

	selectionSort(arr, sizeOfArray);

	cout << "\nsorted array: ";
	for (int i = 0; i < sizeOfArray; i++) {
		cout << arr[i] << " ";
	}
}
