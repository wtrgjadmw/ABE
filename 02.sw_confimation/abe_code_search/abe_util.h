#include <stdio.h>
#include <relic.h>
#include <abe.h>

#ifndef ABE_UTIL_H
#define ABE_UTIL_H

/* ---------------------------------------Standard Operation--------------------------------------- */
void get_stdin(char* s);
void sha256_hash(uint8_t* out_str, uint8_t* in_str);
void print_hex(uint8_t *msg, int msg_len);

/* ---------------------------------------Policy Process--------------------------------------- */
int plc_string_info_init(plc_info_t *PLC_INFO, uint8_t* in_str);
int plc_string_info(plc_info_t *PLC_INFO, uint8_t *in_str);
int split_str_plc(uint8_t **split_att, int* n_split, int* split_type, uint8_t *in_str);
int plc_hash(uint8_t* out_str, uint8_t* in_str, plc_info_t PLC_INFO);

/* ---------------------------------------Check If Policy is Satisfied--------------------------------------- */
int check_plc_sat(int* log_sat, uint8_t **sat_att_list, int* sat_att_no, uint8_t* in_plc, abe_key_t KEY, plc_info_t PLC_INFO);

/* ---------------------------------------Converting Policy to Matrix--------------------------------------- */
int str_plc_to_vec(int **plc_mat, uint8_t **att_list, int *vec, int *vec_len, int* u_temp, int* t_temp, uint8_t* in_str, plc_info_t PLC_INFO);
int str_plc_to_mat(int **plc_mat, uint8_t **att_list, int* u, int* t, uint8_t* in_str, plc_info_t PLC_INFO);

/* ---------------------------------------Det/Inv Matrix--------------------------------------- */
float det_mat(float **inmat, int size);
int inv_mat(float **outmat, float **inmat, int size);

/* ---------------------------------------Number Attribute--------------------------------------- */
void int2bin(uint8_t* binary, int integer, int n);
int plc_2_plcnum (uint8_t* plcnum, int* n_num_plc, uint8_t* in_str);
int plc_all_2_plcnum (uint8_t* out_str, uint8_t* in_str, plc_info_t PLC_INFO);
int att_2_attnum(uint8_t **attnum, int* n_num_att, uint8_t* in_str, int max_att_len);
void user_att_2_attnum(uint8_t **user_attnum, uint8_t **user_att,int n_att, int max_att_len);

/* ---------------------------------------MSG ENC DEC--------------------------------------- */
int aes_kdf_enc(uint8_t *out, int *out_len, uint8_t *in, int in_len, gt_t gt);
int aes_kdf_dec(uint8_t *out, int *out_len, uint8_t *in, int in_len, gt_t gt);


#endif
