#include <time.h>
#include <string.h>
#include <stdio.h>

#define EVE_TIME_INSTANCE 80
#define EVE_NAME_LEN 30

#ifndef ABE_TIME_H
#define ABE_TIME_H

/* ---------------------------------------Time Measurement--------------------------------------- */
long int timespec_sub(struct timespec *t1, struct timespec *t2);
int event(int opt, char *in_eve_name);

#endif
