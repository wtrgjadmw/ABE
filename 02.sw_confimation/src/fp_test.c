#include <stdio.h>
#include <relic.h>
#include "relic_core.h"

/* ---------------------------------------RELIC PARAM SET--------------------------------------- */
int init_param_set(void) {
	if (core_init() != RLC_OK) {
		core_clean();
		return RLC_ERR;
	}

	if (ep_param_set_any() != RLC_OK) {
		RLC_THROW(ERR_NO_CURVE);
		core_clean();
		return RLC_ERR;
	}

	ep_param_print();
	return RLC_OK;
}

void print_hex(uint8_t *msg, int msg_len) {
	for (int i = 0; i < msg_len; i++) {
	    printf("%02X", msg[i]);
	}
	printf("\n");
}

/* ---------------------------------------MAIN--------------------------------------- */
int main() {
	if (init_param_set() != RLC_OK) {
		core_clean();
		return 1;
	}

	fp_t t0,t1,r,r2;
	fp_null(r);
	fp_new(r);
	fp_null(r2);
	fp_new(r2);

	fp_null(t0);
	fp_new(t0);
	fp_rand(t0);
	printf("t0=\n");
	fp_print(t0);

	fp_null(t1);
	fp_new(t1);
	fp_rand(t1);
	printf("t1=\n");
	fp_print(t1);

	fp_add(r, t0, t1);
	printf("add=\n");
	fp_print(r);

	fp_sub(r, t0, t1);
	printf("sub=\n");
	fp_print(r);

	fp_mul(r, t0, t1);
	printf("mul=\n");
	fp_print(r);

	fp_sqr(r, t0);
	printf("sqr=\n");
	fp_print(r);

	fp_srt(r2, r);
	printf("r2 (should equal t0)=\n");
	fp_print(r2);

	fp_inv(r, t0);
	printf("inv=\n");
	fp_print(r);

	return 0;
}
