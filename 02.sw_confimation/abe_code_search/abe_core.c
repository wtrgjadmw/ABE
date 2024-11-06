#include <abe_core.h>

/* ---------------------------------------RELIC PARAM SET--------------------------------------- */
int init_param_set(void) {
	if (core_init() != RLC_OK) {
		core_clean();
		return RLC_ERR;
	}

	if (pc_param_set_any() != RLC_OK) {
		RLC_THROW(ERR_NO_CURVE);
		core_clean();
		return RLC_ERR;
	}

	//pc_param_print();
	return RLC_OK;
}

/* ---------------------------------------SET UP--------------------------------------- */
int abe_mk_set(mpk_t *MPK, msk_t *MSK) {
	bn_t n;
	bn_t alp,del;

	g1_null(MPK->P);
	g2_null(MPK->Q);
	g1_null(MPK->P_del);
	gt_null(MPK->gamma);
	g1_null(MSK->P_alp)
	bn_null(n);
	bn_null(alp);
	bn_null(del);

	g1_new(MPK->P);
	g2_new(MPK->Q);
	g1_new(MPK->P_del);
	gt_new(MPK->gamma);
	g1_new(MSK->P_alp)
	bn_new(n);
	bn_new(alp);
	bn_new(del);

	RLC_TRY {
		event(1,"var_null_new");
		ep_curve_get_ord(n);
		event(1,"ep_curve_get_ord");
		g1_rand(MPK->P);			/* P */
		event(2,"g1_rand");
		g2_rand(MPK->Q);			/* Q */
		event(2,"g2_rand");
		bn_rand_mod(alp, n);			/* alpha */
		bn_rand_mod(del, n);			/* delta */
		event(1,"bn_rand_mod");
		g1_mul(MSK->P_alp, MPK->P, alp);	/* P_alp = [alp]P */
		g1_mul(MPK->P_del, MPK->P, del);	/* P_del = [del]P */
		event(2,"g1_mul");

		pc_map(MPK->gamma,MSK->P_alp,MPK->Q);	/* gamma_temp = e([alp]P,Q) = e(P,Q)^alp  */
		event(2,"pc_map");
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
		abe_mpk_free(MPK);
		abe_msk_free(MSK);
		bn_free(n);
		bn_free(alp);
		bn_free(del);
		return ABE_ERR_RLC;
	}

	bn_free(n);
	bn_free(alp);
	bn_free(del);

	return ABE_NO_ERR;
}

int abe_mpk_free(mpk_t *MPK) {
	RLC_TRY {
		g1_free(MPK->P);
		g2_free(MPK->Q);
		g1_free(MPK->P_del);
		gt_free(MPK->gamma);
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
		return ABE_ERR_RLC;
	}

	return ABE_NO_ERR;
}

int abe_msk_free(msk_t *MSK) {
	RLC_TRY {
		g1_free(MSK->P_alp)
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
		return ABE_ERR_RLC;
	}

	return ABE_NO_ERR;
}

/* ---------------------------------------ENCRYPTION--------------------------------------- */
int abe_ct_set(abe_ct_t *CT, mpk_t MPK, uint8_t *plc, uint8_t *msg, int msg_len, plc_info_t PLC_INFO) {
	int **S_mat = malloc(PLC_INFO.n_att * sizeof(int*));
	for(int i=0; i<PLC_INFO.n_att; i++) {
		S_mat[i] = calloc(PLC_INFO.n_att, sizeof(int*));
	}

	uint8_t **att_map = malloc(PLC_INFO.n_att * sizeof(uint8_t *));
	for(int i=0; i<PLC_INFO.n_att; i++) {
		att_map[i] = malloc(2*ATT_HASH_LEN+1);
	}

	int u,t;
	event(1,"param_alloc");
	str_plc_to_mat(S_mat, att_map, &u, &t, plc, PLC_INFO);
	event(1,"str_plc_to_mat");
	CT->n_att = PLC_INFO.n_att;

	int enc_len,in_len;

	CT->str_plc = malloc(strlen((char*)plc));
	strcpy((char*)CT->str_plc,(char*)plc);

	bn_t s_y[t];		/* s_y[0] = s, s_y[i!=0] = random */
	bn_t lambda[u];	/* share secret */
	bn_t x[u];		/* Random for mixing in g2 */
	bn_t bn_temp, n;
	g1_t g1_temp;

	for (int i=0; i<t; i++) {
		bn_null(s_y[i]);
		bn_new(s_y[i]);
	}
	for (int i=0; i<u; i++) {
		bn_null(lambda[i]);
		bn_null(x[i]);
		bn_new(lambda[i]);
		bn_new(x[i]);
	}
	bn_null(bn_temp);
	bn_new(bn_temp);
	bn_null(n);
	bn_new(n);
	g1_null(g1_temp);
	g1_new(g1_temp);
	event(1,"param_set");
	RLC_TRY {
		ep_curve_get_ord(n);
		event(1,"ep_curve_get_ord");
		for (int i=0; i<t; i++) {
			bn_rand_mod(s_y[i], n);
		}
		for (int i=0; i<u; i++) {
			bn_rand_mod(x[i], n);
			bn_zero(lambda[i]);		/* lambda[i] = 0 */
			for (int j=0; j<t; j++) {
				bn_mul_dig(bn_temp, s_y[j], S_mat[i][j]);		/* bn_temp = S_mat[i][j]*s_y[j]  */
				bn_add(lambda[i], lambda[i], bn_temp);		/* lambda[i] += bn_temp */
			}
		}
		event(1,"bn_operation");
		gt_exp(CT->C, MPK.gamma, s_y[0]);	/* C = gamma^s */
		event(2,"gt_exp");
		gt_inv(CT->C,CT->C);			/* C = gamma^(-s) */
		event(1,"gt_inv");

		in_len = msg_len;
		enc_len = ((in_len/AES_BYTE_LEN)+1)*AES_BYTE_LEN;
		CT->enc_msg = malloc(enc_len);
		aes_kdf_enc(CT->enc_msg, &enc_len, msg,in_len, CT->C);
		CT->enc_len = enc_len;
		event(1,"aes_kdf_enc");
		g2_mul(CT->C_d, MPK.Q, s_y[0]);	/* C_d = [s]Q */
		event(2,"g2_mul");
		CT->C_i = malloc(PLC_INFO.n_att * sizeof(g1_t));
		CT->D_i = malloc(PLC_INFO.n_att * sizeof(g2_t));
		event(1,"malloc");
		for (int i=0; i<u; i++) {
			g1_map(g1_temp, att_map[i], strlen((char*)att_map[i]));	/* Hash(att) */
			event(2,"g1_map");
			g1_mul(g1_temp, g1_temp, x[i]);			/* g1_temp = [x_i]Hash(att) */
			g1_mul(CT->C_i[i], MPK.P_del, lambda[i]);		/* C_i = [lambda_i]P_del */
			event(2,"g1_mul");
			g1_sub(CT->C_i[i], CT->C_i[i], g1_temp);		/* C_i = [lambda_i]P_del - [x_i]Hash(att) */
			event(2,"g1_sub");
			g2_mul(CT->D_i[i], MPK.Q, x[i]);			/* D_i = [x_i]Q */
			event(2,"g2_mul");
		}
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
	}

	bn_free(bn_temp);
	bn_free(n);
	g1_free(g1_temp);
	for (int i=0; i<t; i++) {
		bn_free(s_y[i]);
	}
	for (int i=0; i<u; i++) {
		bn_free(x[i]);
		bn_free(lambda[i]);
	}

	for(int i=0; i<PLC_INFO.n_att; i++) {
		free(S_mat[i]);
	}
	free(S_mat);

	for(int i=0; i<PLC_INFO.n_att; i++) {
		free(att_map[i]);
	}
	free(att_map);

	return 0;
}

int abe_ct_free(abe_ct_t *CT) {
	RLC_TRY {
		free(CT->str_plc);
		free(CT->enc_msg);
		g2_free(CT->C_d);
		for(int i=0;i<CT->n_att;i++) {
			g1_free(CT->C_i[i]);
			g2_free(CT->D_i[i]);
		}
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
		return ABE_ERR_RLC;
	}

	return ABE_NO_ERR;
}

/* ---------------------------------------KEY GEN--------------------------------------- */
int abe_key_set(abe_key_t *KEY, mpk_t MPK, msk_t MSK, uint8_t **user_att, int n_att) {
	bn_t tao;
	bn_t n;
	g1_t g1_temp;

	bn_null(tao);
	bn_null(n);
	g1_null(g1_temp);
	bn_new(tao);
	bn_new(n);
	g1_new(g1_temp);
	event(1,"abe_key_set_param_set");
	RLC_TRY {
		KEY->n_att = n_att;
		ep_curve_get_ord(n);
		bn_rand_mod(tao, n);
		event(1,"bn");
		g1_mul(g1_temp, MPK.P_del, tao);	/* g1_temp = [tao]P_del */
		event(2,"g1_mul");
		g1_add(KEY->K, MSK.P_alp, g1_temp);	/* K = P_alp + [tao]P_del */
		event(2,"g1_add");
		g2_mul(KEY->L, MPK.Q, tao);		/* L = [tao]Q */
		event(2,"g2_mul");

		KEY->K_i = malloc(n_att * sizeof(g1_t));
		KEY->att_i = malloc(n_att * sizeof(KEY->att_i));
		for(int i=0; i<n_att; i++) {
			KEY->att_i[i] = malloc(2*ATT_HASH_LEN+1);
		}
		event(1,"alloc");
		for (int i=0; i<n_att; i++) {
			sha256_hash(KEY->att_i[i], user_att[i]);
			event(1,"sha256_hash");
			g1_map(g1_temp, KEY->att_i[i], strlen((char*)KEY->att_i[i]));	/* Hash(att) */
			event(2,"g1_map");
			g1_mul(KEY->K_i[i], g1_temp, tao);				/* K_i = [tao]Hash(att) */
			event(2,"g1_mul");
		}
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
	}
	/*
	printf("checkparamkey\n");
	g1_norm(KEY->K,KEY->K);
	g1_print(KEY->K);
	g2_print(KEY->L);
	g1_print(KEY->K_i[0]);
	g1_print(KEY->K_i[1]);*/

	bn_free(tao);
	bn_free(n);
	g1_free(g1_temp);

	return 0;
}

int abe_key_free(abe_key_t *KEY) {
	RLC_TRY {
		g1_free(KEY->K);
		g2_free(KEY->L);
		for(int i=0;i<KEY->n_att;i++) {
			g1_free(KEY->K_i[i]);
			free(KEY->att_i[i]);
		}
		free(KEY->att_i);
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
		return ABE_ERR_RLC;
	}

	return ABE_NO_ERR;
}

/* ---------------------------------------DECRYPT--------------------------------------- */
int abe_decrypt(uint8_t* out_msg, int* dec_len, gt_t output, abe_ct_t CT, abe_key_t KEY) {
	int n_match=0;
	int max_n_match = (KEY.n_att < CT.n_att ? KEY.n_att : CT.n_att);
	int *dec_att_map_pol = malloc(max_n_match * sizeof(int*));
	int *dec_att_map_key = malloc(max_n_match * sizeof(int*));

	int log_sat,sat_att_no;
	uint8_t **sat_att_list = malloc(max_n_match * sizeof(uint8_t *));
	for(int i=0; i<max_n_match; i++) {
		sat_att_list[i] = malloc(ATT_HASH_LEN*2+1);
	}

	plc_info_t PLC_INFO;
	plc_string_info_init(&PLC_INFO, CT.str_plc);
	plc_string_info(&PLC_INFO, CT.str_plc);

	check_plc_sat(&log_sat, sat_att_list, &sat_att_no, CT.str_plc, KEY, PLC_INFO);


	//Check check_plc_sat function
	//printf("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n");
	//printf("log_sat: %d sat_att_no:%d\n",log_sat,sat_att_no);
	//for (int i=0;i<sat_att_no;i++) {
	//	printf("Satisfy att no.%d is: %s\n",i,sat_att_list[i]);
	//}

	//printf("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n");

	if (log_sat == 0) {
		strcpy((char*)out_msg,"");
		printf("User attributes do not satisfy policy\n");
		return -1;
	}
	event(1,"check_plc_sat");

	// Matrix Creation
	int **S_mat = malloc(PLC_INFO.n_att * sizeof(int*));
	for(int i=0; i<PLC_INFO.n_att; i++) {
		S_mat[i] = calloc(PLC_INFO.n_att, sizeof(int*));
	}

	uint8_t **att_map = malloc(PLC_INFO.n_att * sizeof(uint8_t *));
	for(int i=0; i<PLC_INFO.n_att; i++) {
		att_map[i] = malloc(2*ATT_HASH_LEN+1);
	}

	int u,t;

	str_plc_to_mat(S_mat, att_map, &u, &t, CT.str_plc, PLC_INFO);
	event(1,"str_plc_to_mat");

	//printf("sat_att_no:%d t:%d\n",sat_att_no,t);
	// User Matrix Creation
	int **S_user_mat_temp = malloc(sat_att_no * sizeof(int*));
	float **S_user_mat = malloc(sat_att_no * sizeof(float*));
	float **w_mat_temp = malloc(sat_att_no * sizeof(float*));
	for(int i=0; i<sat_att_no; i++) {
		S_user_mat_temp[i] = calloc(t, sizeof(int*));
		S_user_mat[i] = calloc(sat_att_no, sizeof(float*));
		w_mat_temp[i] = calloc(sat_att_no, sizeof(float*));
	}

	for (int i=0;i<u;i++) {
	//check from CT if match or not
		for (int j=0;j<sat_att_no;j++) {
			if (strcmp((char*)sat_att_list[j],(char*)att_map[i])==0) {
			//If Key attribute match CT attribute
				for (int k=0;k<t;k++) {
					S_user_mat_temp[n_match][k] = S_mat[i][k];
				}

				dec_att_map_pol[n_match] = i;
				for (int l=0;l<KEY.n_att;l++) {
					if (strcmp((char*)KEY.att_i[l],(char*)att_map[i])==0) {
						dec_att_map_key[n_match] = l;
						break;
					}
				}
				n_match++;
			}
		}
	}
	event(1,"User_Matrix_Creation");

	//printf("n_match: %d\n",n_match);
	/*for (int i=0;i<n_match;i++) {
		printf("dec_att_map_pol[%d]: %d dec_att_map_key[%d]: %d\n",i,dec_att_map_pol[i],i,dec_att_map_key[i]);
	}
	printf("S_user_mat_temp:\n");
	for (int i=0;i<n_match;i++) {
		for (int j=0;j<t;j++) {
			printf("%d ",S_user_mat_temp[i][j]);
		}
		printf("\n");
	}*/

	//Require function to cut matrix into square matrix
	int copy_f; //Flag for column copy
	int copy_ind=0; //Index for column copy

	for (int j=0;j<t;j++) {
		copy_f=0;
		for (int i=0;i<n_match;i++) {
			copy_f+=S_user_mat_temp[i][j];
		}

		if (copy_f!=0) {
			for (int i=0;i<n_match;i++) {
				S_user_mat[i][copy_ind] = S_user_mat_temp[i][j];
			}
			copy_ind++;
		}
	}
	event(1,"User_Matrix_to_Square");

	//printf("[CONFIRMATION] copy_ind == n_match == sat_att_no %d:%d:%d\n",copy_ind,n_match,sat_att_no);

	/*printf("S_user_mat:\n");
	for (int i=0;i<n_match;i++) {
		for (int j=0;j<n_match;j++) {
			printf("%f ",S_user_mat[i][j]);
		}
		printf("\n");
	}*/

	//Inverse matrix
	int S_det;
	S_det=(int)det_mat(S_user_mat, n_match);
	//printf("S_det: %d\n",S_det);

	if (S_det!=0) {
		inv_mat(w_mat_temp, S_user_mat, n_match);
	} else {
		printf("ERROR S_det = 0\n");
	}
	event(1,"inverse_matrix");
	/*
	printf("Inverse S_user_mat (w_mat_temp):\n");
	for (int i=0;i<n_match;i++) {
		for (int j=0;j<n_match;j++) {
			printf("%f ",w_mat_temp[i][j]);
		}
		printf("\n");
	}*/

	//Create bn_t matrix w[i]
	int temp;
	bn_t bn_det;
	bn_null(bn_det);
	bn_new(bn_det);

	bn_t n;
	bn_null(n);
	bn_new(n);
	ep_curve_get_ord(n);

	bn_t w[n_match];
	for (int i=0;i<n_match;i++) {
		bn_null(w[i]);
		bn_new(w[i]);
	}

	for (int i=0;i<n_match;i++) {
		temp=(int)(w_mat_temp[0][i]*S_det);
		//printf("temp: %d\n",temp);
		if(temp >= 0){
			bn_zero(w[i]);
			bn_add_dig(w[i],w[i],temp);
		} else {
			bn_sub_dig(w[i],n,-temp);
		}
		//printf("w[%d]:\n",i);
		//bn_print(w[i]);
	}

	if (S_det > 0) {
		bn_zero(bn_det);
		bn_add_dig(bn_det,bn_det,S_det);
	} else if (S_det < 0) {
		bn_sub_dig(bn_det,n,S_det);
		//bn_print(bn_det);
	}
	event(1,"bn_operation");

	//map_sim
	ep_t *_p = RLC_ALLOCA(ep_t, n_match+2);
	ep2_t *_q = RLC_ALLOCA(ep2_t, n_match+2);

	g1_t g1_temp1, g1_temp2, g1_temp3;

	g1_null(g1_temp1);
	g1_null(g1_temp2);
	g1_null(g1_temp3);

	g1_new(g1_temp1);
	g1_new(g1_temp2);
	g1_new(g1_temp3);
	event(1,"var_null_new");

	printf("n_match:[%d]",n_match);
	RLC_TRY {
		if (_p == NULL || _q == NULL) {
			RLC_THROW(ERR_NO_MEMORY);
		}
		for (int i = 0; i < n_match+2; i++) {
			ep_null(_p[i]);
			ep2_null(_q[i]);
			ep_new(_p[i]);
			ep2_new(_q[i]);
		}

		bn_det->used=4; //grow n_bits to 192? not enough but cannot grow to 256. dk why but should be figure out later
		g1_mul(g1_temp1, KEY.K, bn_det);		/* g1_temp1 = [det]K */
		event(2,"g1_mul");
		g1_neg(_p[0], g1_temp1);			/* g1_temp1 = -[det]K */
		event(2,"g1_neg");
		g2_copy(_q[0], CT.C_d);
		event(2,"g12_copy");

		g1_set_infty(g1_temp2);
		event(1,"g1_set_infty");
		for (int i=0; i<n_match; i++) {
			w[i]->used=4; //grow n_bits to 192? not enough but cannot grow to 256. dk why but should be figure out later
			// printf("wi: [%d]%d\n",w[i]->used,bn_bits(w[i]));
			// bn_print(w[i]);
			g1_mul(g1_temp1, CT.C_i[dec_att_map_pol[i]], w[i]);	/* g1_temp1 = [w_i]C_i */
			event(2,"g1_mul");
			g1_add(g1_temp2, g1_temp2, g1_temp1);	/* g1_temp2 += {sigma}[w_i]C_i */
			event(2,"g1_add");
		}

		g1_copy(_p[1], g1_temp2);
		g2_copy(_q[1], KEY.L);
		event(2,"g12_copy");

		for (int i=0; i<n_match; i++) {
			g1_mul(g1_temp3, KEY.K_i[dec_att_map_key[i]], w[i]);		/* g1_temp3 = [w_i]K_i */
			event(2,"g1_mul");
			g1_copy(_p[2+i], g1_temp3);
			g2_copy(_q[2+i], CT.D_i[dec_att_map_pol[i]]);
			event(2,"g12_copy");
		}
		pc_map_sim(output, _p, _q, n_match+2);
		event(2,"pc_map");

		/* Final exponentiation with det */
		//bn_print(bn_det);
		bn_mod_inv(bn_det,bn_det,n);		/* bn_det = 1/[det] */
		event(1,"bn_mod_inv");
		//bn_print(bn_det);
		gt_exp(output,output,bn_det);
		event(2,"gt_exp");

		//Use output to derive key and decrypt and recover message.
		(*dec_len) = CT.enc_len;
		aes_kdf_dec(out_msg, dec_len, CT.enc_msg, CT.enc_len, output);
		out_msg[*dec_len] = '\0';
		event(1,"aes_kdf_dec");
	}
	RLC_CATCH_ANY {
		RLC_THROW(ERR_CAUGHT);
	}

	//Free Memory
	g1_free(g1_temp1);
	g1_free(g1_temp2);
	g1_free(g1_temp3);

	for (int i = 0; i < n_match+2; i++) {
		ep_free(_p[i]);
		ep2_free(_q[i]);
	}
	RLC_FREE(_p);
	RLC_FREE(_q);

	for(int i=0; i<max_n_match; i++) {
		free(sat_att_list[i]);
	}
	free(sat_att_list);
	for(int i=0; i<PLC_INFO.n_att; i++) {
		free(S_mat[i]);
	}
	free(S_mat);
	for(int i=0; i<PLC_INFO.n_att; i++) {
		free(att_map[i]);
	}
	free(att_map);
	for(int i=0; i<sat_att_no; i++) {
		free(S_user_mat_temp[i]);
		free(S_user_mat[i]);
		free(w_mat_temp[i]);
	}
	free(S_user_mat_temp);
	free(S_user_mat);
	free(w_mat_temp);
	return 0;
}

/* ---------------------------------------Export/Import Parameters to/from Files--------------------------------------- */
int parti_phrase(char out[PART_LEN], char *in) {
	if(strlen(in)<PART_LEN) {
		strcpy(out,in);
		for (int i=0;i<PART_LEN-strlen(in)-1;i++) {
			strcat(out,"+");
		}
	} else {
		strncpy(out,in,PART_LEN-1);
	}
	out[PART_LEN-1]='\0';
	return 0;
}

int parti_len(char out[PART_LEN], int x) {
	int length = snprintf(NULL, 0, "%d", x);
	char int_str[PART_LEN];

	if(length<PART_LEN) {
		snprintf(int_str, length + 1, "%d", x );
		strcpy(out,int_str);
		for (int i=0;i<PART_LEN-length-1;i++) {
			strcat(out,"+");
		}
	} else {
		return 1;
	}
	out[PART_LEN-1]='\0';
	return 0;
}

int parti_len_read(int *x, char in[PART_LEN]) {
	char int_str[PART_LEN];

	for (int i=0;i<PART_LEN;i++) {
		if (in[i]!='+') {
			int_str[i]=in[i];
		} else {
			int_str[i]='\0';
			break;
		}
	}
	*x = strtol(int_str, (char **)NULL, 10);

	return 0;
}

int abe_mpk_exp(char *fname, mpk_t *MPK) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN],bin_g2[BIN_G2_LEN],bin_gt[BIN_GT_LEN];

	fp = fopen(fname, "w");
	parti_phrase(partitioner, "ABE_MPK");
	fwrite(partitioner,PART_LEN, 1,fp);

	/* P */
	g1_write_bin(bin_g1, BIN_G1_LEN, MPK->P, POINT_BIN_COMP);
	fwrite(bin_g1,BIN_G1_LEN,1,fp);

	/* Q */
	g2_write_bin(bin_g2, BIN_G2_LEN, MPK->Q, POINT_BIN_COMP);
	fwrite(bin_g2,BIN_G2_LEN,1,fp);

	/* P_del */
	g1_write_bin(bin_g1, BIN_G1_LEN, MPK->P_del, POINT_BIN_COMP);
	fwrite(bin_g1,BIN_G1_LEN,1,fp);

	/* gamma */
	gt_write_bin(bin_gt, BIN_GT_LEN, MPK->gamma, POINT_BIN_COMP);
	fwrite(bin_gt,BIN_GT_LEN,1,fp);

	fclose(fp);

	return 0;
}

int abe_mpk_imp(mpk_t *MPK, char *fname) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN],bin_g2[BIN_G2_LEN],bin_gt[BIN_GT_LEN];

	fp = fopen(fname, "r");
	fread(partitioner,PART_LEN,1,fp);

	/* P */
	fread(bin_g1,BIN_G1_LEN,1,fp);
	g1_read_bin(MPK->P, bin_g1, BIN_G1_LEN);

	/* Q */
	fread(bin_g2,BIN_G2_LEN,1,fp);
	g2_read_bin(MPK->Q, bin_g2, BIN_G2_LEN);

	/* P_del */
	fread(bin_g1,BIN_G1_LEN,1,fp);
	g1_read_bin(MPK->P_del, bin_g1, BIN_G1_LEN);

	/* gamma */
	fread(bin_gt,BIN_GT_LEN,1,fp);
	gt_read_bin(MPK->gamma, bin_gt, BIN_GT_LEN);

	fclose(fp);

	return 0;
}

int abe_msk_exp(char *fname, msk_t *MSK) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN];

	fp = fopen(fname, "w");
	parti_phrase(partitioner, "ABE_MSK");
	fwrite(partitioner,PART_LEN, 1,fp);

	/* P_alp */
	g1_write_bin(bin_g1, BIN_G1_LEN, MSK->P_alp, POINT_BIN_COMP);
	fwrite(bin_g1,BIN_G1_LEN,1,fp);

	fclose(fp);

	return 0;
}

int abe_msk_imp(msk_t *MSK, char *fname) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN];

	fp = fopen(fname, "r");
	fread(partitioner,PART_LEN,1,fp);

	/* P_alp */
	fread(bin_g1,BIN_G1_LEN,1,fp);
	g1_read_bin(MSK->P_alp, bin_g1, BIN_G1_LEN);

	fclose(fp);

	return 0;
}

int abe_ct_exp(char *fname, abe_ct_t *CT) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN],bin_g2[BIN_G2_LEN];

	fp = fopen(fname, "w");
	parti_phrase(partitioner, "ABE_CT");
	fwrite(partitioner,PART_LEN, 1,fp);

	/* str_plc */
	parti_len(partitioner, strlen((char*)CT->str_plc));
	fwrite(partitioner,PART_LEN, 1,fp);
	fwrite((char*)CT->str_plc,strlen((char*)CT->str_plc), 1,fp);

	/* enc_msg */
	parti_len(partitioner,CT->enc_len);
	fwrite(partitioner,PART_LEN, 1,fp);
	fwrite((char*)CT->enc_msg,CT->enc_len, 1,fp);

	/* End text */
	parti_phrase(partitioner, "End text");
	fwrite(partitioner,PART_LEN, 1,fp);

	/* C_d */
	g2_write_bin(bin_g2, BIN_G2_LEN, CT->C_d, POINT_BIN_COMP);
	fwrite(bin_g2,BIN_G2_LEN,1,fp);

	/* n_att */
	parti_len(partitioner, CT->n_att);
	fwrite(partitioner,PART_LEN, 1,fp);

	/* C_i and D_i */
	for (int i=0;i<CT->n_att;i++) {
		g1_write_bin(bin_g1, BIN_G1_LEN, CT->C_i[i], POINT_BIN_COMP);
		fwrite(bin_g1,BIN_G1_LEN,1,fp);
		g2_write_bin(bin_g2, BIN_G2_LEN, CT->D_i[i], POINT_BIN_COMP);
		fwrite(bin_g2,BIN_G2_LEN,1,fp);
	}

	fclose(fp);

	return 0;
}

int abe_ct_imp(abe_ct_t *CT, char *fname) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN],bin_g2[BIN_G2_LEN];
	int str_len;

	fp = fopen(fname, "r");
	if(fp == NULL) {
		printf("Error importing ABE CT file\n");
		return RLC_ERR;
	}

	fread(partitioner,PART_LEN,1,fp);

	/* str_plc */
	fread(partitioner,PART_LEN,1,fp);
	parti_len_read(&str_len, partitioner);
	CT->str_plc = malloc(str_len+1);
	fread((char*)CT->str_plc,str_len,1,fp);
	CT->str_plc[str_len]='\0';

	/* enc_msg */
	fread(partitioner,PART_LEN,1,fp);
	parti_len_read(&str_len, partitioner);
	CT->enc_len = str_len;
	CT->enc_msg = malloc(str_len+1);
	fread((char*)CT->enc_msg,str_len,1,fp);

	/* End text */
	fread(partitioner,PART_LEN,1,fp);

	/* C_d */
	fread(bin_g2,BIN_G2_LEN,1,fp);
	g2_read_bin(CT->C_d, bin_g2, BIN_G2_LEN);

	/* n_att */
	fread(partitioner,PART_LEN,1,fp);
	parti_len_read(&(CT->n_att), partitioner);

	/* C_i and D_i */
	CT->C_i = malloc(CT->n_att * sizeof(g1_t));
	CT->D_i = malloc(CT->n_att * sizeof(g2_t));
	for (int i=0;i<CT->n_att;i++) {
		fread(bin_g1,BIN_G1_LEN,1,fp);
		g1_read_bin(CT->C_i[i], bin_g1, BIN_G1_LEN);
		fread(bin_g2,BIN_G2_LEN,1,fp);
		g2_read_bin(CT->D_i[i], bin_g2, BIN_G2_LEN);
	}

	fclose(fp);

	return 0;
}

int abe_key_exp(char *fname, abe_key_t *KEY) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN],bin_g2[BIN_G2_LEN];

	fp = fopen(fname, "w");
	parti_phrase(partitioner, "ABE_KEY");
	fwrite(partitioner,PART_LEN, 1,fp);

	/* K */
	g1_write_bin(bin_g1, BIN_G1_LEN, KEY->K, POINT_BIN_COMP);
	fwrite(bin_g1,BIN_G1_LEN,1,fp);

	/* L */
	g2_write_bin(bin_g2, BIN_G2_LEN, KEY->L, POINT_BIN_COMP);
	fwrite(bin_g2,BIN_G2_LEN,1,fp);

	/* n_att */
	parti_len(partitioner, KEY->n_att);
	fwrite(partitioner,PART_LEN, 1,fp);

	/* K_i and att_i */
	for (int i=0;i<KEY->n_att;i++) {
		g1_write_bin(bin_g1, BIN_G1_LEN, KEY->K_i[i], POINT_BIN_COMP);
		fwrite(bin_g1,BIN_G1_LEN,1,fp);

		//parti_len(partitioner, strlen((char*)KEY->att_i[i]));
		//fwrite(partitioner,PART_LEN, 1,fp);
		fwrite((char*)KEY->att_i[i],strlen((char*)KEY->att_i[i]), 1,fp);
	}

	fclose(fp);

	return 0;
}

int abe_key_imp(abe_key_t *KEY, char *fname) {
	FILE *fp;
	char partitioner[PART_LEN];
	uint8_t bin_g1[BIN_G1_LEN],bin_g2[BIN_G2_LEN];
	int str_len;

	fp = fopen(fname, "r");
	fread(partitioner,PART_LEN,1,fp);

	/* K */
	fread(bin_g1,BIN_G1_LEN,1,fp);
	g1_read_bin(KEY->K, bin_g1, BIN_G1_LEN);

	/* L */
	fread(bin_g2,BIN_G2_LEN,1,fp);
	g2_read_bin(KEY->L, bin_g2, BIN_G2_LEN);

	/* n_att */
	fread(partitioner,PART_LEN,1,fp);
	parti_len_read(&(KEY->n_att), partitioner);

	/* K_i and att_i */
	KEY->K_i = malloc(KEY->n_att * sizeof(g1_t));
	KEY->att_i = malloc(KEY->n_att * sizeof(KEY->att_i));
	str_len = 2*ATT_HASH_LEN;
	for (int i=0;i<KEY->n_att;i++) {
		fread(bin_g1,BIN_G1_LEN,1,fp);
		g1_read_bin(KEY->K_i[i], bin_g1, BIN_G1_LEN);

		//fread(partitioner,PART_LEN,1,fp);
		//parti_len_read(&str_len, partitioner);
		KEY->att_i[i] = malloc(str_len+1);
		fread((char*)KEY->att_i[i],str_len,1,fp);
		KEY->att_i[i][str_len]='\0';
	}

	fclose(fp);

	return 0;
}

/* --------------PRINT-------------- */
void print_mpk(mpk_t MPK) {
	printf("Showing Master Public Key Parameters\n");
	printf("MPK.P:\n");
	g1_print(MPK.P);
	printf("MPK.Q:\n");
	g2_print(MPK.Q);
	printf("MPK.P_del:\n");
	g1_print(MPK.P_del);
	printf("MPK.gamma:\n");
	gt_print(MPK.gamma);
	printf("\n");
}

void print_msk(msk_t MSK) {
	printf("Showing Master Secret Key Parameters\n");
	printf("MSK.P_alp:\n");
	g1_print(MSK.P_alp);
	printf("\n");
}

void print_ct(abe_ct_t CT) {
	printf("Showing Ciphertext Parameters\n");
	printf("CT.str_plc:\n");
	printf("%s\n",CT.str_plc);
	printf("CT.C:\n"); //Need remove
	gt_print(CT.C); //Need remove
	printf("CT.enc_msg:\n");
	printf("%s\n",CT.enc_msg);
	printf("CT.enc_msg[hex]:\n");
	print_hex(CT.enc_msg,strlen((char*)CT.enc_msg));
	printf("CT.C_d:\n");
	g2_print(CT.C_d);
	printf("CT.n_att:\n");
	printf("%d\n",CT.n_att);
	for(int i=0;i<CT.n_att;i++) {
		printf("CT.C_i[%d]:\n",i);
		g1_print(CT.C_i[i]);
		printf("CT.D_i[%d]:\n",i);
		g2_print(CT.D_i[i]);
	}
	printf("\n");
}

void print_key(abe_key_t KEY) {
	printf("Showing Key Parameters\n");
	printf("KEY.K:\n");
	g1_print(KEY.K);
	printf("KEY.L:\n");
	g2_print(KEY.L);
	printf("KEY.n_att:\n");
	printf("%d\n",KEY.n_att);
	for(int i=0;i<KEY.n_att;i++) {
		printf("KEY.K_i[%d]:\n",i);
		g1_print(KEY.K_i[i]);
		printf("KEY.att_i[%d]:\n",i);
		printf("%s\n",KEY.att_i[i]);
	}
}
