#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char * argv[]) {

  
const int DIM = 100;
    int v[DIM];
    for (int i=0; i<DIM; i++) {
        v[i]=rand() % 1000;
    }
int s=0;
for(int i=0; i<DIM; i++){
    s=s + v[i];
    cout<< s<< endl <<endl;}
    
    //Ora qui avete un vettore di DIM elementi che
    //contiene valori tra 0 e 999 (1000 escluso)

   cout<<"codice che calcola 10 valori di v"<<endl<<endl;
    int v1[10];
for(int i=0; i<10; i++){
   v1[i]=0;
   cout<< i << endl;}

   //fate un ciclo 10000000 di iterazioni
   cout <<"il ciclo da 10000000 di iterazioni!!!"
 <<endl;
 for (int i= 0; i< 10000000; i++)
{
    int r=rand()%10;
    v1[r]= v1[r]+1;
    } 

    for (int i=0; i<10; i++){
        cout<<v1[i]<<endl;
    }
    
      return 0;
}

