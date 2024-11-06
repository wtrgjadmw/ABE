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

	ep_t p;
	ep_null(p);
	ep_new(p);
	ep_rand(p);

	printf("p\n");
	ep_print(p);

	bn_t n;
	bn_t k;
	bn_null(n);
	bn_new(n);
	bn_null(k);
	bn_new(k);
	ep_curve_get_ord(n);
	bn_print(n);
	fp_prime_get_par(k);
	bn_print(k);

	dig_t prime;
	prime=fp_prime_get();
	fp_print(prime);

	fp_t aa,bb;
	fp_null(aa);
	fp_new(aa);
	fp_zero(aa);
	fp_null(bb);
	fp_new(bb);
	fp_zero(bb);;
	fp_add(aa, aa, ep_curve_get_a());
	fp_add(bb, bb, ep_curve_get_b());
	printf("a=\n");
	fp_print(aa);
	printf("b=\n");
	fp_print(bb);

	return 0;
}
