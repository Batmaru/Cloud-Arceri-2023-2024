#include <iostream>
#include <cstdio>


using namespace std;

int main(int argc, char * argv[]) {

  
const int DIM = 100;
    int v[DIM];
    for (int i=0; i<DIM; i++) {
        v[i]=rand() % 1000;
    }


    //Ora qui avete un vettore di DIM elementi che
    //contiene valori tra 0 e 999 (1000 escluso)
    return 0;
}