#include <stdio.h>
int main(){
    int T, N;
    scanf_S("%d", &T);
    for (int i=1; i<=T; i++){
        scanf_s("%d", &N);
        int min=100000;
        int count=0;
        for(int j=0; j<N; j++){
            int location;
            scanf_s("%d", &location);
            if(location<0){
                location=-location;
            }
            if(min>location){
                min=location;
                count=1;
            }
            else if(min==location){
                count+=1;
            }
            else{}
        }
        printf("#%d %d %d", i, min, count);
    }
}