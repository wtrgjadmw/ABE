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

void ep_add_edit(ep_t r, const ep_t p, const ep_t q) {

	fp_t t0, t1, t2, t3, t4, t5;

	fp_null(t0);
	fp_null(t1);
	fp_null(t2);
	fp_null(t3);
	fp_null(t4);
	fp_null(t5);

	RLC_TRY {
		fp_new(t0);
		fp_new(t1);
		fp_new(t2);
		fp_new(t3);
		fp_new(t4);
		fp_new(t5);

		/* Formulas for point addition from
		 * "Complete addition formulas for prime order elliptic curves"
		 * by Joost Renes, Craig Costello, and Lejla Batina
		 * https://eprint.iacr.org/2015/1060.pdf
		 */
		fp_mul(t0, p->x, q->x);
		fp_mul(t1, p->y, q->y);
		fp_mul(t2, p->z, q->z);
		fp_add(t3, p->x, p->y);
		fp_add(t4, q->x, q->y);
		fp_mul(t3, t3, t4);
		fp_add(t4, t0, t1);
		fp_sub(t3, t3, t4);
		if (ep_curve_opt_a() == RLC_MIN3) {
			/* Cost of 12M + 2m_b + 29a. */
			fp_add(t4, p->y, p->z);
			fp_add(t5, q->y, q->z);
			fp_mul(t4, t4, t5);
			fp_add(t5, t1, t2);
			fp_sub(t4, t4, t5);
			fp_add(r->x, p->x, p->z);
			fp_add(r->y, q->x, q->z);
			fp_mul(r->x, r->x, r->y);
			fp_add(r->y, t0, t2);
			fp_sub(r->y, r->x, r->y);
			ep_curve_mul_b(r->z, t2);
			fp_sub(r->x, r->y, r->z);
			fp_dbl(r->z, r->x);
			fp_add(r->x, r->x, r->z);
			fp_sub(r->z, t1, r->x);
			fp_add(r->x, t1, r->x);
			ep_curve_mul_b(r->y, r->y);
			fp_dbl(t1, t2);
			fp_add(t2, t1, t2);
			fp_sub(r->y, r->y, t2);
			fp_sub(r->y, r->y, t0);
			fp_dbl(t1, r->y);
			fp_add(r->y, t1, r->y);
			fp_dbl(t1, t0);
			fp_add(t0, t1, t0);
			fp_sub(t0, t0, t2);
			fp_mul(t1, t4, r->y);
			fp_mul(t2, t0, r->y);
			fp_mul(r->y, r->x, r->z);
			fp_add(r->y, r->y, t2);
			fp_mul(r->x, t3, r->x);
			fp_sub(r->x, r->x, t1);
			fp_mul(r->z, t4, r->z);
			fp_mul(t1, t3, t0);
			fp_add(r->z, r->z, t1);
		}

		r->coord = PROJC;
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
	}
	RLC_FINALLY {
		fp_free(t0);
		fp_free(t1);
		fp_free(t2);
		fp_free(t3);
		fp_free(t4);
		fp_free(t5);
	}

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
	fp_read_str(t0->x, "ED0718DF99C450479DF19D2BACAC58F38F86777EABC16B4230384797040C10104FB4B1D70CA24F173CF7912F43B63531", 96, 16);
	fp_read_str(t0->y, "654DA63AD090ECB1639037BCCA2AE129A943367E61D667D3EA1AD40B0819ECBDAC109DB935F70C1D5B4A2308E9978F46", 96, 16);
	printf("t0=\n");
	ep_print(t0);

	ep_null(t1);
	ep_new(t1);
	ep_rand(t1);
	fp_read_str(t1->x, "8FA6D7D6195FA91F9F0C953B02117D78540C111F9ED4884FE5E0CDF7A37841B34C44ED5FD712CE0B76C4B772EF442743", 96, 16);
	fp_read_str(t1->y, "F7A60F73706483C521AD2EA6596371972E07DF31B537427C4FDA0E1591EE992825C5EF4434A7B4B405E8D62BEC761D60", 96, 16);
	printf("t1=\n");
	ep_print(t1);

	ep_add(r, t0, t1);
	ep_norm(r,r);
	printf("add=\n");
	ep_print(r);

	ep_sub(r2, r, t1);
	ep_norm(r2,r2);
	printf("sub check=\n");
	ep_print(r2);

	ep_sub(r, t0, t1);
	ep_norm(r,r);
	printf("sub=\n");
	ep_print(r);

	ep_dbl(r, t0);
	ep_norm(r,r);
	printf("dbl=\n");
	ep_print(r);

	bn_t k1,k2,k3,n;
	bn_null(n);
	bn_new(n);
	ep_curve_get_ord(n);

	bn_null(k1);
	bn_new(k1);
	bn_rand_mod(k1,n);
	ep_mul(r,t0,k1);
	printf("mul k1=\n");
	bn_print(k1);
	ep_print(r);

	bn_null(k2);
	bn_new(k2);
	bn_rand_mod(k2,n);
	ep_mul(r,t0,k2);
	printf("mul k2=\n");
	bn_print(k2);
	ep_print(r);

	bn_null(k3);
	bn_new(k3);
	bn_rand_mod(k3,n);
	ep_mul(r,t0,k3);
	printf("mul k3=\n");
	bn_print(k3);
	ep_print(r);

	printf("RLC_MIN3=%d\n",RLC_MIN3);

	return 0;
}
