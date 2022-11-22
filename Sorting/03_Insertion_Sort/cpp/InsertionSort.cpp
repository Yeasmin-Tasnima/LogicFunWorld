#include<iostream>
using namespace std;

void insertionSort(int arr[], int n) {
	for (int i = 1; i < n; i++) {
		int value = arr[i];
		int hole = i;
		while (hole > 0 && arr[hole - 1] > value) {
			arr[hole] = arr[hole - 1];
			hole -= 1;
		}
		arr[hole] = value;
	}
}

int main() {
	int arr[] = { 2, 7, 4, 1, 5, 3 };
	int sizeOfArray = sizeof(arr) / sizeof(int);

	cout << "unsorted array: ";
	for (int i = 0; i < sizeOfArray; i++) {
		cout << arr[i] << " ";
	}

	insertionSort(arr, sizeOfArray);

	cout << "\nsorted array: ";
	for (int i = 0; i < sizeOfArray; i++) {
		cout << arr[i] << " ";
	}
}
