#include <stdio.h>
#include <relic.h>
#include <abe.h>
#include <abe_util.h>

#ifndef ABE_CORE_H
#define ABE_CORE_H

/* ---------------------------------------RELIC PARAM SET--------------------------------------- */
int init_param_set(void);

/* ---------------------------------------SET UP--------------------------------------- */
int abe_mk_set(mpk_t *MPK, msk_t *MSK);
int abe_mpk_free(mpk_t *MPK);
int abe_msk_free(msk_t *MSK);

/* ---------------------------------------ENCRYPTION--------------------------------------- */
int abe_ct_set(abe_ct_t *CT, mpk_t MPK, uint8_t *plc, uint8_t *msg, int msg_len, plc_info_t PLC_INFO);
int abe_ct_free(abe_ct_t *CT);

/* ---------------------------------------KEY GEN--------------------------------------- */
int abe_key_set(abe_key_t *KEY, mpk_t MPK, msk_t MSK, uint8_t **user_att, int n_att);
int abe_key_free(abe_key_t *KEY);

/* ---------------------------------------DECRYPT--------------------------------------- */
int abe_decrypt(uint8_t* out_msg, int* dec_len, gt_t output, abe_ct_t CT, abe_key_t KEY);

/* ---------------------------------------Export/Import Parameters to/from Files--------------------------------------- */
int parti_phrase(char out[PART_LEN], char *in);
int parti_len(char out[PART_LEN], int x);
int parti_len_read(int *x, char out[PART_LEN]);

int abe_mpk_exp(char *fname, mpk_t *MPK);
int abe_mpk_imp(mpk_t *MPK, char *fname);
int abe_msk_exp(char *fname, msk_t *MSK);
int abe_msk_imp(msk_t *MSK, char *fname);
int abe_ct_exp(char *fname, abe_ct_t *CT);
int abe_ct_imp(abe_ct_t *CT, char *fname);
int abe_key_exp(char *fname, abe_key_t *KEY);
int abe_key_imp(abe_key_t *KEY, char *fname);

/* ---------------------------------------Print Structure--------------------------------------- */
void print_mpk(mpk_t MPK);
void print_msk(msk_t MSK);
void print_ct(abe_ct_t CT);
void print_key(abe_key_t KEY);

#endif
