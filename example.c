#include <time.h>
double My_variable = 3.0;

int fact(int n) {
    if (n <= 1) return 1;
    else return n*fact(n-1);
}

int prime(int n) {
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
            return 0;
    }

    return 1;
}

void idle() {

}

int my_mod(int x, int y) {
    return (x%y);
}

char *get_time()
{
    time_t ltime;
    time(&ltime);
    return ctime(&ltime);
}

struct Vector
{
    double x, y, z;
};

extern struct Vector bar;
