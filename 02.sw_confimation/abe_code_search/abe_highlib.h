#include <stdio.h>
#include <relic.h>
#include <abe.h>
#include <abe_util.h>
#include <abe_core.h>

#include <relic.h>

#ifndef ABE_HIGHLIB_H
#define ABE_HIGHLIB_H

/* ---------------------------------------Highlib Option1--------------------------------------- */
int h1_system_setup();
int h1_edit_att();
int h1_user_regis();
int h1_encryption();
int h1_decryption();

/* ---------------------------------------Highlib Option2--------------------------------------- */
int h2_system_setup();
int h2_user_regis();
int h2_encryption();
int h2_decryption();

/* ---------------------------------------Base Operation--------------------------------------- */
int system_setup();
int user_encrypt();
int user_key_gen();
int user_decrypt();

/* ---------------------------------------Text File Enc/Dec--------------------------------------- */
int aes_kdf_file_enc(char *fname, uint8_t *pwd, int option);
int aes_kdf_file_dec(char *fname, uint8_t *pwd, int option);
int abe_file_enc(char *fname, uint8_t *user_input_plc, mpk_t MPK, int option);

/* ---------------------------------------Other hlib Operations--------------------------------------- */
int bin2hex(uint8_t* out , uint8_t* in, int in_len);
int check_user_regis(int* result, uint8_t* username, uint8_t* user_pass);
int get_user_att_data(int* result, char* attdata, int *user_n_att, uint8_t* username);
int user_att_data_to_array(uint8_t** user_att, int user_n_att, char* attdata);
int user_att_assess_for_attnum(int *max_att_len, int *user_n_att, uint8_t** user_att);

#endif
