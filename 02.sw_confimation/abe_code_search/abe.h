#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <relic.h>

/* For Time Measurement*/
#include <abe_time.h>

#ifndef ABE_H
#define ABE_H

/* Error Return Value */
#define ABE_NO_ERR 0
#define ABE_ERR_RLC 1
#define ABE_ERR_OTHER 2

/* File Name */
#define ABE_MPK_FNAME "[ABE]MPK.txt"
#define ABE_MSK_FNAME "[ABE]MSK.txt"
#define ABE_CT_FNAME "[ABE]CT.txt"
#define ABE_KEY_FNAME "[ABE]KEY.txt"
#define ABE_ATTDATA_FNAME "[ABE]AttData.txt"
#define ABE_REGIS_FNAME "[ABE]Regis.txt"
#define ABE_MPK2_FNAME "[ABE]MPK2.txt"
#define ABE_MSK2_FNAME "[ABE]MSK2.txt"

/* Export/Import Parameters to/from Files */
#define PART_LEN 21 //20 + '\0' = 21
#define POINT_BIN_COMP 0 // Import/Export option: 0 for No Compression, 1 for Compression

#if POINT_BIN_COMP == 0
#define BIN_G1_LEN 2*RLC_FP_BYTES+1
#define BIN_G2_LEN 4*RLC_FP_BYTES + 1
#define BIN_GT_LEN 12*RLC_FP_BYTES
#elif POINT_BIN_COMP == 1
#define BIN_G1_LEN RLC_FP_BYTES+1
#define BIN_G2_LEN 2*RLC_FP_BYTES + 1
#define BIN_GT_LEN 10*RLC_FP_BYTES
#endif

/* Policy */
#define ATT_NUM_BIT 8
#define ABE_PLC_AND " AND "
#define ABE_PLC_OR " OR "

/* Other underlying cryptographic parameters */
#define ATT_HASH_LEN 32 /* Parameter for SHA-256 */
#define AES_BYTE_LEN 16 /* Parameter for AES-128 */
#define KDF_LEN 32 /* Parameter for storing user hashed password */

/* File Encryption */
#define F_REMOVE 0
#define F_KEEP 1

/* ABE Data Structure */
typedef struct {
/* Policy String Info for Dynamic Allocation */
	int n_att;		// Number of attribute in policy
	int n_max_split;	// Number of max split in every policy level
	int att_max_size;	// Max len of attribute in the policy
	int n_num_max_att;	// Number of attribute when converted to number policy
	int plc_num_str_size;	// Possible size increment of policy when converted to number policy
	int att_num_max_size;	// Max len of number attribute in the policy
} plc_info_t;

typedef struct {
/* ABE Master Public Key */
	g1_t P;
	g2_t Q;
	g1_t P_del;
	gt_t gamma;
} mpk_t;

typedef struct {
/* ABE Master Secret Key */
	g1_t P_alp;
} msk_t;

typedef struct {
/* Ciphertext */
	uint8_t *str_plc;
	gt_t C; //Need remove
	int enc_len;
	uint8_t *enc_msg;
	g2_t C_d;
	int n_att;
	g1_t *C_i;
	g2_t *D_i;
} abe_ct_t;

typedef struct {
/* KEY */
	g1_t K;
	g2_t L;
	int n_att;
	g1_t *K_i;
	uint8_t **att_i;
} abe_key_t;

#endif
