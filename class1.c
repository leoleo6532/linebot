#include <stdio.h> 
#include <stdlib.h> 
int n;

int main(void) { 

  printf("½Ð¿é¤J¶¥­¼:");  
  scanf("%d",&n);
  int fact(int n);
  int ans = fact(n);
  printf("%d",ans);

}


int fact(int n){

    int f;
    if(n==0) return 1;
    f = fact(n-1);
    return(n*f);
}
