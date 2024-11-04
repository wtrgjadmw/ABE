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

	ep_t t0,t1,r,r2;
	ep_null(r);
	ep_new(r);
	ep_null(r2);
	ep_new(r2);

	ep_null(t0);
	ep_new(t0);
	ep_rand(t0);
	fp_read_str(t0->x, "140a5ad03a5e3278cd3875d6220d79f822f9da36d89a296bb9fd7ab5224b6092caaaa80bcb152eaa79427b5fdc769423", 96, 16);
	fp_read_str(t0->y, "079282942f8938d0979cc1256e79b6acc36d4f56b2af5148c1b657a73d4feb0a11157c6f40df3cd9c6e44c6da09a2cae", 96, 16);
	printf("t0=\n");
	ep_print(t0);

	// ep_null(t1);
	// ep_new(t1);
	// ep_rand(t1);
	// fp_read_str(t1->x, "8FA6D7D6195FA91F9F0C953B02117D78540C111F9ED4884FE5E0CDF7A37841B34C44ED5FD712CE0B76C4B772EF442743", 96, 16);
	// fp_read_str(t1->y, "F7A60F73706483C521AD2EA6596371972E07DF31B537427C4FDA0E1591EE992825C5EF4434A7B4B405E8D62BEC761D60", 96, 16);
	// printf("t1=\n");
	// ep_print(t1);

	// ep_add(r, t0, t1);
	// ep_norm(r,r);
	// printf("add=\n");
	// ep_print(r);
	//
	// ep_sub(r2, r, t1);
	// ep_norm(r2,r2);
	// printf("sub check=\n");
	// ep_print(r2);
	//
	// ep_sub(r, t0, t1);
	// ep_norm(r,r);
	// printf("sub=\n");
	// ep_print(r);
	//
	// ep_dbl(r, t0);
	// ep_norm(r,r);
	// printf("dbl=\n");
	// ep_print(r);

	bn_t k1,k2,k3,n;
	bn_null(n);
	bn_new(n);
	ep_curve_get_ord(n);

	bn_null(k1);
	bn_new(k1);
	bn_read_str(k1, "3658105680CCE9174F05423C534F60E0345DCE5BB58EB3C260633D3D09766313", 64, 16);
	// bn_rand_mod(k1,n);
	ep_mul(r,t0,k1);
	printf("mul k1=\n");
	bn_print(k1);
	ep_print(r);

	// bn_null(k2);
	// bn_new(k2);
	// bn_rand_mod(k2,n);
	// ep_mul(r,t0,k2);
	// printf("mul k2=\n");
	// bn_print(k2);
	// ep_print(r);
	//
	// bn_null(k3);
	// bn_new(k3);
	// bn_rand_mod(k3,n);
	// ep_mul(r,t0,k3);
	// printf("mul k3=\n");
	// bn_print(k3);
	// ep_print(r);
	//
	// printf("RLC_MIN3=%d\n",RLC_MIN3);

	return 0;
}
