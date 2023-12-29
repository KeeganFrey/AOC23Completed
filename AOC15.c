#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hash(char c, int *curval);

int main(){
    char word[20] = "", ch = ' ';
    int hsh = 0, n = 0, sum = 0;
    FILE *fin = fopen("input15.txt","r");
    if(fin == NULL){
        fprintf(stdout, "Error in opening the file");
    }else{
        while(fscanf(fin, "%c", &ch) != EOF){
            if(ch==','){
            hsh = 0, n  = strlen(word);
            for(int i = 0; i<n; i++){
                hash(word[i], &hsh);
                word[i] = '\0';
            }
            sum = sum+hsh;
            n = 0;
            }
            else{
                word[n] = ch;
                n++;
            }
       }
    }
    fclose(fin);
    fprintf(stdout,"%d",sum);
}

void hash(char c, int *curval){
    int i = c;
    *curval+=i;
    *curval*=17;
    *curval %= 256;
}