#include <stdio.h>
#include <relic.h>
#include "relic_core.h"

#define ATT_HASH_LEN 32

void sha256_hash(uint8_t* out_str, uint8_t* in_str) {
	//"abc" = ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
	uint8_t digest[ATT_HASH_LEN];
	uint8_t digest_temp[3];
	strcpy((char*)out_str,"");
	md_map_sh256(digest, in_str, strlen((char *)in_str));
	
	for (int i = 0; i < ATT_HASH_LEN; i++)
	{
	    sprintf((char*)digest_temp,"%02X", digest[i]);
	    strcat((char*)out_str,(char*)digest_temp);
	}
	out_str[2*ATT_HASH_LEN]='\0';
}

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

	// uint8_t in_str[] = "Hello, World!";
	// uint8_t out_str[2*ATT_HASH_LEN];

	// sha256_hash(out_str, in_str);

	// printf("SHA-256 Hash: ");
    // print_hex(out_str, sizeof(out_str));

	// g1_map(g1_temp, out_str, strlen((char*)out_str));	/* Hash(att) */

	g1_t g1_temp;
	uint8_t msg[] = "abc";
	printf("msg: %s\n",msg);
	uint8_t dst[] = "QUUX-V01-CS02-BLS12381G1_XMD:SHA-256_SSWU_RO_";
	printf("dst: %s\n",dst);
	ep_map_dst(g1_temp, msg, sizeof(msg), dst, sizeof(dst));
	printf("result point:\n");
	g1_print(g1_temp);

	printf("\n\n");

	g1_t g1_temp2;
	// ep_map_dst --------------
	const int len_per_elm = (FP_PRIME + ep_param_level() + 7) / 8;
	uint8_t *pseudo_random_bytes = RLC_ALLOCA(uint8_t, 2 * len_per_elm);
	md_xmd(pseudo_random_bytes, 2 * len_per_elm, msg, sizeof(msg), dst, sizeof(dst));
	printf("len_per_elm: %d\n",len_per_elm);
	printf("pseudo_random_bytes (128 byte = 1024 bit):\n");
	print_hex(pseudo_random_bytes, 2 * len_per_elm);

	bn_t k;
	fp_t t;
	ep_t q;
	bn_null(k);
	fp_null(t);
	ep_null(q);
	bn_new(k);
	fp_new(t);
	ep_new(q);

	bn_read_bin(k, pseudo_random_bytes + 0 * len_per_elm, len_per_elm);
    fp_prime_conv(t, k);   
	printf("prime field (1):\n");
	fp_print(t);
	bn_read_bin(k, pseudo_random_bytes + 1 * len_per_elm, len_per_elm);
    fp_prime_conv(t, k);   
	printf("prime field (2):\n");
	fp_print(t);

	const char *a_str, *b_str, *xn_str, *xd_str, *yn_str, *yd_str, *u_str;

	ep_param_set_ctmap(a_str, b_str, xn_str, xd_str, yn_str, yd_str, u_str);
	printf(a_str);
	printf(b_str);
	printf(u_str);

	ep_map_from_field(g1_temp2, pseudo_random_bytes, 2 * len_per_elm);
	RLC_FREE(pseudo_random_bytes);
	// ep_map_dst --------------
	printf("result point:\n");
	g1_print(g1_temp2);

	return 0;
}
