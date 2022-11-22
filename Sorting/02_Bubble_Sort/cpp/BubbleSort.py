#include<iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
	for (int i = 0; i < n - 1; i++) {
		int flag = 0;
		for (int j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
				flag = 1;
			}
		}
		if (flag == 0) {
			break;
		}
	}
}

int main() {
	int arr[] = { 2, 7, 4, 1, 5, 3 };
	int sizeOfArray = sizeof(arr) / sizeof(int);

	cout << "unsorted array: ";
	for (int i = 0; i < sizeOfArray; i++) {
		cout << arr[i] << " ";
	}

	bubbleSort(arr, sizeOfArray);

	cout << "\nsorted array: ";
	for (int i = 0; i < sizeOfArray; i++) {
		cout << arr[i] << " ";
	}
}
