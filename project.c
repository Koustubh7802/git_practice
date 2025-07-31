#include <stdio.h>

int main(){
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};

    for(int i=0; i<10; i++){
        printf("%p\n",arr+i);
    }
    int x = sizeof(arr[0]);
    printf("%d",x);
    return 0;
}