#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cti(char in);

int main (){
    FILE * fin = fopen("input1.txt", "r");
    if(fin == NULL){
        fprintf(stdout,"Problem opening file");
    }else{
        char curline[100] = "";
        int count = 0, sum = 0,num = 0, n = 0, rightn = 0, leftn = 0, ll = 0, lr = 0, numl = 0, numr = 0,tnl=0,tnr=0; 
        while(fscanf(fin, "%s", curline) != EOF){
                n = strlen(curline);
                //get ones
                rightn = n;
                while(curline[rightn]<48||curline[rightn]>57){
                    rightn--;
                }
                //get tens
                leftn = 0;
                while(curline[leftn]<48||curline[leftn]>57){
                    leftn++;
                }
                num = cti(curline[leftn])*10 + cti(curline[rightn]);
                sum += num;
                count++;
        }
        fprintf(stdout, "%d", sum);
    }
    fclose(fin); 
}

int cti(char in){
    int a = -1;
    switch(in){
        case (48):
        a = 0;
        break;
        case (49):
        a = 1;
        break;
        case (50):
        a = 2;
        break;
        case (51):
        a = 3;
        break;
        case (52):
        a = 4;
        break;
        case (53):
        a = 5;
        break;
        case (54):
        a = 6;
        break;
        case (55):
        a = 7;
        break;
        case (56):
        a = 8;
        break;
        case (57):
        a = 9;
        break;
    }
    return a;
}
