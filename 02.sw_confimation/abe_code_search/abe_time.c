#include <abe_time.h>

#define VERBOSE 0
#define IMP_EVE_TIME_INSTANCE 10
//Measurement in nanosec
/* ---------------------------------------Time Measurement--------------------------------------- */
long int timespec_sub(struct timespec *t1, struct timespec *t2)
{
	long int total_ns;
	total_ns = ((t1->tv_sec - t2->tv_sec)*1000000000) + (t1->tv_nsec - t2->tv_nsec);
	return total_ns;
}

int event(int opt, char *in_eve_name) {
	//opt==0:Initialize, opt==1:Input event, opt==2:Input important event, opt==3:End
	static int eve_cnt;
	static long int eve_time[EVE_TIME_INSTANCE];
	static char eve_name[EVE_TIME_INSTANCE][EVE_NAME_LEN];
	static struct timespec t_now,t_past;
	static char process_name[EVE_NAME_LEN];

	static int imp_eve;
	static long int imp_eve_time[EVE_TIME_INSTANCE];
	static long int imp_eve_number_called[EVE_TIME_INSTANCE];
	static char imp_eve_name[IMP_EVE_TIME_INSTANCE][EVE_NAME_LEN] = {
    {"g1_map"},
		{"g1_rand"},
    {"g1_mul"},
		{"g2_rand"},
		{"g2_mul"},
    {"gt_exp"},
    {"pc_map"},
		{"g1_add"},
		{"g1_sub"},
		{"others"}
	};

	// char out[EVE_NAME_LEN];
	long int total_time1,total_time2;
	int i,j;

	if(opt==0) {
		//Initialize all parameters
		eve_cnt = 0;
		imp_eve = 0;
		for (i=0;i<EVE_TIME_INSTANCE;i++) {
			eve_time[i] = 0;
			imp_eve_time[i] = 0;
			imp_eve_number_called[i] = 0;
			for (j=0;j<EVE_NAME_LEN;j++) {
				eve_name[i][j]='\0';
			}
		}
		strcpy(process_name, in_eve_name);
		clock_gettime(CLOCK_MONOTONIC, &t_past);
		//printf("CLOCK_MONOTONIC %ld %ld\n",t_past.tv_sec,t_past.tv_nsec);
	} else if (opt==1) {
		//Marks the end of event and its name
		clock_gettime(CLOCK_MONOTONIC, &t_now);

		eve_time[eve_cnt] = timespec_sub(&t_now, &t_past);
		strcpy(eve_name[eve_cnt], in_eve_name);
		eve_cnt++;
		clock_gettime(CLOCK_MONOTONIC, &t_past);
		//printf("CLOCK_MONOTONIC %ld %ld\n",t_past.tv_sec,t_past.tv_nsec);
	} else if (opt==2) {
		imp_eve = 1;
		clock_gettime(CLOCK_MONOTONIC, &t_now);
		for(i=0;i<IMP_EVE_TIME_INSTANCE-1;i++) {
		// Need to -1 because if not meet i will be the index for others category
			if (strcmp(in_eve_name,imp_eve_name[i])==0) {
				break;
			}
		}
		if(VERBOSE){
			// if(i==0){ //g1_map
			// 	printf("g1_map time: %lld.%.9ld\n", (long long)t_now.tv_sec, t_now.tv_nsec);
			// }
			if(i==2){ //g1_mul
				printf("g1_mul comp time: %ld\n", timespec_sub(&t_now, &t_past));
			}
		}
		imp_eve_time[i] += timespec_sub(&t_now, &t_past);
		imp_eve_number_called[i]++;
		clock_gettime(CLOCK_MONOTONIC, &t_past);
	} else if (opt==3) {
		//End of measurement and print the result
		printf("==%s==================",process_name);
		total_time1 = 0;
		printf("[");
		for (i=0;i<eve_cnt;i++) {
			printf("%s/",eve_name[i]);
		}
		printf("]: ");
		for (i=0;i<eve_cnt;i++) {
			printf("%ld ",eve_time[i]);
			total_time1 += eve_time[i];
		}

		total_time2 = 0;

		if(imp_eve == 1) {
			printf("[");
			for (int i=0;i<IMP_EVE_TIME_INSTANCE;i++) {
				printf("%s/",imp_eve_name[i]);
			}
			printf("]: ");
			for (int i=0;i<IMP_EVE_TIME_INSTANCE;i++) {
				printf("%ld ",imp_eve_time[i]);
				total_time2 += imp_eve_time[i];
			}
		}
		printf("[NotECCTotal/ECCTotal/AllTotal]: %ld %ld %ld\n",total_time1,total_time2,total_time1+total_time2);

		if(VERBOSE) {
			printf("\nTime Called: ");
			for (int i=0;i<IMP_EVE_TIME_INSTANCE;i++) {
				printf("%s: %ld\n",imp_eve_name[i],imp_eve_number_called[i]);
			}
		}
	}
	return 0;
}

/*
event(0,"Process Name");
...
event(1,"bn_rand");
...
event(1,"scalar_mul");
event(2,"");

*/
