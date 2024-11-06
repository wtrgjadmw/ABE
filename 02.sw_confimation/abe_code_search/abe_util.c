#include <stdio.h>
#include <abe_util.h>

/* ---------------------------------------Standard Input--------------------------------------- */
void get_stdin(char* s) {
//Get one line input from user
	char buf[BUFSIZ];
	char *p;
	
	if (fgets(buf, sizeof(buf), stdin) != NULL) {
		if ((p = strchr(buf, '\n')) != NULL) {
			*p = '\0';
		}
	}
	
	strcpy(s,buf);
}

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

void print_hex(uint8_t *msg, int msg_len) {
	for (int i = 0; i < msg_len; i++) {
	    printf("%02X", msg[i]);
	}
	printf("\n");
}

/* ---------------------------------------Policy Process--------------------------------------- */
int plc_string_info_init(plc_info_t *PLC_INFO, uint8_t* in_str) {
	PLC_INFO->n_att=0;
	PLC_INFO->n_max_split=0;
	PLC_INFO->att_max_size=0;
	PLC_INFO->n_num_max_att=0;
	PLC_INFO->plc_num_str_size=strlen((char*)in_str)+1;
	PLC_INFO->att_num_max_size=0;
	return 0;
}

int plc_string_info(plc_info_t *PLC_INFO, uint8_t *in_str) {
	int n=1; //At least 1 and increment with AND or OR
	uint8_t *pos_ptr;
	int pos=0;
	while(pos!=-1){
		pos_ptr = (uint8_t*)strstr((char*)in_str+pos+1, ABE_PLC_AND);
		pos = (pos_ptr == NULL ? -1 : pos_ptr - in_str);
		n = (pos_ptr == NULL ? n : n+1);
	}
	pos=0;
	while(pos!=-1){
		pos_ptr = (uint8_t*)strstr((char*)in_str+pos+1, ABE_PLC_OR);
		pos = (pos_ptr == NULL ? -1 : pos_ptr - in_str);
		n = (pos_ptr == NULL ? n : n+1);
	}
	
	uint8_t **split_att = malloc(n * sizeof(uint8_t *));
	for(int i=0; i<n; i++) {
		split_att[i] = malloc(strlen((char*)in_str)+1);
	}
	
	int n_split = 0;
	int split_type;
	uint8_t str_temp[strlen((char*)in_str)];
	strcpy((char*)str_temp,(char*)in_str);
	int num=0;
	
	split_str_plc(split_att, &n_split, &split_type, str_temp);
	if(n_split > PLC_INFO->n_max_split) {
		PLC_INFO->n_max_split = n_split;
	}
	
	if (split_type == 2) {
		(PLC_INFO->n_att)+=1;
		if(strlen((char*)str_temp) > PLC_INFO->att_max_size) {
			PLC_INFO->att_max_size = strlen((char*)str_temp)+1;
		}
		if(strlen((char*)str_temp) > PLC_INFO->att_num_max_size) {
			PLC_INFO->att_num_max_size = strlen((char*)str_temp)+1;
		}
		pos_ptr = (uint8_t*)strchr((char*)str_temp, '=');
		num = (pos_ptr == NULL ? num : num+1);
		pos_ptr = (uint8_t*)strchr((char*)str_temp, '>');
		num = (pos_ptr == NULL ? num : num+1);
		pos_ptr = (uint8_t*)strchr((char*)str_temp, '<');
		num = (pos_ptr == NULL ? num : num+1);
		if(num!=0) {
			(PLC_INFO->n_num_max_att)+=8;
			(PLC_INFO->plc_num_str_size)+= (8*(strlen((char*)str_temp)+ATT_NUM_BIT)+7*(strlen(ABE_PLC_AND)+2));
			if((strlen((char*)str_temp)+1+ATT_NUM_BIT) > PLC_INFO->att_num_max_size) {
				PLC_INFO->att_num_max_size = strlen((char*)str_temp)+ATT_NUM_BIT;
			}
		} else {
			(PLC_INFO->n_num_max_att)+=1;
		}
	} else if (split_type == 0 || split_type == 1) {
	//Case AND or OR
		for (int i=0;i<n_split;i++) {
			plc_string_info(PLC_INFO, split_att[i]);
		}
	}
	
	for (int i = 0; i < n; i++) {
		free(split_att[i]);
	}
	free(split_att);
	
	return 0;
}

int split_str_plc(uint8_t **split_att, int* n_split, int* split_type, uint8_t *in_str) {
	uint8_t str[strlen((char*)in_str)];
	strcpy((char*)str,(char*)in_str);
	uint8_t str2[strlen((char*)in_str)]; //for temporary value of string copy
	uint8_t *pos_ptr;
	int count_op_br, count_cl_br, len;
	int AND_pos,OR_pos,op_br_pos,cl_br_pos;
	int op_br_pos2, cl_br_pos2, next_inc;
	uint8_t search_AND[] = ABE_PLC_AND;
	uint8_t search_OR[] = ABE_PLC_OR;
	int search_word_skip,search_word_pos;
	
	len = strlen((char*)in_str);
	
	int i=0;
	while(1) {
		pos_ptr = (uint8_t*)strchr((char*)str,'(');
		op_br_pos = (pos_ptr == NULL ? -1 : pos_ptr - str);
	
		if (op_br_pos == 0) {
			count_op_br = 1;
			count_cl_br = 0;
			next_inc = 0;
			
			while (count_op_br - count_cl_br != 0) {
				pos_ptr = (uint8_t*)strchr((char*)str + next_inc + 1,'(');
				op_br_pos2 = (pos_ptr == NULL ? -1 : pos_ptr - str);
				pos_ptr = (uint8_t*)strchr((char*)str + next_inc + 1,')');
				cl_br_pos2 = (pos_ptr == NULL ? -1 : pos_ptr - str);
				
				if (op_br_pos2 == -1 && cl_br_pos2 != -1) {
				//Case no more '('. But there is ')' so count close bracket.
					count_cl_br++;
					next_inc = cl_br_pos2;
				} else if (op_br_pos2 != -1 && cl_br_pos2 != -1) {
				//Case find both '(' and ')'
					if (op_br_pos2 < cl_br_pos2) {
						count_op_br++;
						next_inc = op_br_pos2;
					} else {
						count_cl_br++;
						next_inc = cl_br_pos2;
					}
				} else {
				//Case no more '(' and ')'. Case find '(' but no ')'. Input error.
					printf("Input string error1\n");
					cl_br_pos = len-2;
					break;
				}
			}
			cl_br_pos = cl_br_pos2;
			
			if (cl_br_pos == len-1) {
			//Case str start with '(' and end with ')'. Repeat the step again while striped of first '(' and last ')'.
				if (i !=0) {
				//Start '(' and end with ')' after splitting some string already mean they should stay together.
					strcpy((char*)str2,(char*)str+1);
					strcpy((char*)str, (char*)str2);
					str[len-2] = '\0';
					strcpy((char*)split_att[i], (char*)str);
					*n_split = i+1;
					break;
				} else {
				//Else mean that there is extra '(' and ')' which convey no meaning. Strip and repeat with extra free iteration. 
					i--;
					strcpy((char*)str2,(char*)str+1);
					strcpy((char*)str, (char*)str2);
					str[len-2] = '\0';
					len = strlen((char*)str);
				}
			} else {
			//Case str start with '(' but but not end with ')'.
				pos_ptr = (uint8_t*)strstr((char*)str+cl_br_pos+1, (char*)search_AND);
				AND_pos = (pos_ptr == NULL ? -1 : pos_ptr - str);
				pos_ptr = (uint8_t*)strstr((char*)str+cl_br_pos+1, (char*)search_OR);
				OR_pos = (pos_ptr == NULL ? -1 : pos_ptr - str);
				
				//Need to confirm that AND or OR start after ')'.
				if (AND_pos !=1 && AND_pos-cl_br_pos == 1) {
					//printf("find AND\n");
					*split_type = 1;
					search_word_skip = strlen((char*)search_AND);
				} else if (OR_pos !=1 && OR_pos-cl_br_pos == 1) {
					*split_type = 0;
					search_word_skip = strlen((char*)search_OR);
				} else {
				//Input error.
					printf("Input string error2\n");
					strcpy((char*)split_att[i], (char*)str);
					*n_split = i+1;
					break;
				}
				
				strncpy((char*)split_att[i], (char*)str + 1, cl_br_pos-1);
				split_att[i][cl_br_pos-1] = '\0';
				strcpy((char*)str2, (char*)str+ cl_br_pos + search_word_skip+1);
				strcpy((char*)str, (char*)str2);
				len = strlen((char*)str);
			}
			
		} else {
			pos_ptr = (uint8_t*)strstr((char*)str, (char*)search_AND);
			AND_pos = (pos_ptr == NULL ? -1 : pos_ptr - str);
			pos_ptr = (uint8_t*)strstr((char*)str, (char*)search_OR);
			OR_pos = (pos_ptr == NULL ? -1 : pos_ptr - str);
			
			//Need to confirm that AND or OR start after ')'.
			if (AND_pos != -1 && (op_br_pos == -1 || AND_pos < op_br_pos)) {
				*split_type = 1;
				search_word_skip = strlen((char*)search_AND);
				search_word_pos = AND_pos;
			} else if (OR_pos != -1 && (op_br_pos == -1 || OR_pos < op_br_pos)) {
				*split_type = 0;
				search_word_skip = strlen((char*)search_OR);
				search_word_pos = OR_pos;
			} else {
			//End of splitting string
				if (i==0) {
					*split_type = 2;
				}
				strcpy((char*)split_att[i], (char*)str);
				*n_split = i+1;
				break;
			}
			
			strncpy((char*)split_att[i], (char*)str, search_word_pos);
			split_att[i][search_word_pos] = '\0';
			strcpy((char*)str2, (char*)str+search_word_pos+search_word_skip);
			strcpy((char*)str, (char*)str2);
			len = strlen((char*)str);
		}
		i++;
	}
	
	
	return 0;
}

int plc_hash(uint8_t* out_str, uint8_t* in_str, plc_info_t PLC_INFO) {
//If plc_all_2_plcnum is run before need to run plc_string_info again to update n_max_split and n_att
	uint8_t **split_att = malloc(PLC_INFO.n_max_split * sizeof(uint8_t *));
	for(int i=0; i<PLC_INFO.n_max_split; i++) {
		split_att[i] = malloc(strlen((char*)in_str));
	}
	int n_split = 0;
	int split_type;
	uint8_t str_temp[strlen((char*)in_str)];
	strcpy((char*)str_temp,(char*)in_str);
	// Each attribute will take [2*ATT_HASH_LEN] and maximum of between character is '(','')' and " AND "
	uint8_t *temp = malloc(PLC_INFO.n_att * (2*ATT_HASH_LEN) + (PLC_INFO.n_att-1)*(strlen(ABE_PLC_AND)+2));
	uint8_t *out_temp = malloc(PLC_INFO.n_att * (2*ATT_HASH_LEN) + (PLC_INFO.n_att-1)*(strlen(ABE_PLC_AND)+2));
	uint8_t hex_digest[2*ATT_HASH_LEN+1];
	
	split_str_plc(split_att, &n_split, &split_type, str_temp);
	
	if (split_type == 2) {
		sha256_hash(hex_digest, str_temp);
		strcpy((char*)out_temp,(char*)hex_digest);
	} else if (split_type == 0) {
	//Case OR
		strcpy((char*)out_temp,"");
		strcat((char*)out_temp,"(");
		for (int i=0;i<n_split;i++) {
			plc_hash(temp, split_att[i], PLC_INFO);
			strcat((char*)out_temp,(char*)temp);
			if(i==n_split-1) {
				strcat((char*)out_temp,")");
			} else {
				strcat((char*)out_temp,ABE_PLC_OR);
			}
		}
	} else if (split_type == 1) {
	//Case AND
		strcpy((char*)out_temp,"");
		strcat((char*)out_temp,"(");
		for (int i=0;i<n_split;i++) {
			plc_hash(temp, split_att[i], PLC_INFO);
			strcat((char*)out_temp,(char*)temp);
			if(i==n_split-1) {
				strcat((char*)out_temp,")");
			} else {
				strcat((char*)out_temp,ABE_PLC_AND);
			}
		}
	}
	strcpy((char*)out_str,(char*)out_temp);
	
	for (int i = 0; i < PLC_INFO.n_max_split; i++) {
		free(split_att[i]);
	}
	free(split_att);
	free(out_temp);
	free(temp);
	
	return 0;
}

/* ---------------------------------------Check If Policy is Satisfied--------------------------------------- */
int check_plc_sat(int* log_sat, uint8_t **sat_att_list, int* sat_att_no, uint8_t* in_plc, abe_key_t KEY, plc_info_t PLC_INFO) {
	uint8_t **split_att = malloc(PLC_INFO.n_max_split * sizeof(uint8_t *));
	for(int i=0; i<PLC_INFO.n_max_split; i++) {
		split_att[i] = malloc(strlen((char*)in_plc));
	}
	int n_split = 0;
	int split_type;
	int min_att_no = KEY.n_att;
	int log_sat_temp1 = 0,log_sat_temp2 = 0;

	uint8_t **sat_att_list_temp1 = malloc(KEY.n_att * sizeof(uint8_t *));
	for(int i=0; i<KEY.n_att; i++) {
		sat_att_list_temp1[i] = calloc(2*ATT_HASH_LEN+1,sizeof(uint8_t));
	}
	uint8_t **sat_att_list_temp2 = malloc(KEY.n_att * sizeof(uint8_t *));
	for(int i=0; i<KEY.n_att; i++) {
		sat_att_list_temp2[i] = calloc(2*ATT_HASH_LEN+1,sizeof(uint8_t));
	}
	
	int sat_att_no_temp1 = 0,sat_att_no_temp2 = 0;
	
	//printf("in str: %s\n",in_plc);
	split_str_plc(split_att, &n_split, &split_type, in_plc);
	
	if (split_type == 2) {
	//Case 'attribute'
		//check if there is the matched attribute in KEY
		(*log_sat) = 0;
		for (int i=0;i<KEY.n_att;i++) {
			if (strcmp((char*)KEY.att_i[i],(char*)in_plc)==0) {
				strcpy((char*)sat_att_list[0],(char*)KEY.att_i[i]);
				(*sat_att_no)=1;
				(*log_sat) = 1;
				break;
			}
		}		
	} else if (split_type == 0){
	//Case OR
		log_sat_temp1 = 0;
		for (int i=0;i<n_split;i++) {
			log_sat_temp2 = 0;
			check_plc_sat(&log_sat_temp2, sat_att_list_temp2, &sat_att_no_temp2, split_att[i], KEY, PLC_INFO);
			//printf("[OR] sat?: %d split_att: %s\n",log_sat_temp2,split_att[i]);
			if (log_sat_temp2 == 1) {
			//If this branch satisfy
				log_sat_temp1 = 1;
				if (sat_att_no_temp2 < min_att_no) {
				//If number of sat att is lesser then use this set instead
					min_att_no = sat_att_no_temp2;
					for(int j =0;j<sat_att_no_temp2;j++) {
						strcpy((char*)sat_att_list_temp1[j],(char*)sat_att_list_temp2[j]);
					}
				}
			}
		}
		
		//After check all split put result into return parameter
		*log_sat = log_sat_temp1;
		if (log_sat_temp1 == 0) {
		//Case not satisfy
			min_att_no = 0;
			*sat_att_no = 0;
		} else {
			*sat_att_no = min_att_no;
			for(int i=0;i<min_att_no;i++) {
				strcpy((char*)sat_att_list[i],(char*)sat_att_list_temp1[i]);
			}
		}
	} else if (split_type == 1){
	//Case AND
		log_sat_temp1 = 1;
		for (int i=0;i<n_split;i++) {
			log_sat_temp2 = 0;
			check_plc_sat(&log_sat_temp2, sat_att_list_temp2, &sat_att_no_temp2, split_att[i], KEY, PLC_INFO);
			//printf("[AND] sat?: %d split_att: %s\n",log_sat_temp2,split_att[i]);
			if (log_sat_temp2 == 0) {
				log_sat_temp1 = 0;
				break;
			} else {
			//If satisy, add all the list into the current list
				for (int j=0;j<sat_att_no_temp2;j++){
					strcpy((char*)sat_att_list_temp1[sat_att_no_temp1+j],(char*)sat_att_list_temp2[j]);
				}
				sat_att_no_temp1+=sat_att_no_temp2;
			}
		}
		
		//After check all split put result into return parameter
		*log_sat = log_sat_temp1;
		if (log_sat_temp1 == 1) {
		//Case all branch satisfy
			*sat_att_no = sat_att_no_temp1;
			for(int i=0;i<sat_att_no_temp1;i++) {
				strcpy((char*)sat_att_list[i],(char*)sat_att_list_temp1[i]);
			}
		} else {
			*sat_att_no = 0;
		}
	}
	
	return 0;
}

/* ---------------------------------------Converting Policy to Matrix--------------------------------------- */
int str_plc_to_vec(int **plc_mat, uint8_t **att_list, int *vec, int *vec_len, int* u_temp, int* t_temp, uint8_t* in_str, plc_info_t PLC_INFO) {
	uint8_t **split_att = malloc(PLC_INFO.n_num_max_att * sizeof(uint8_t *));
	for(int i=0; i<PLC_INFO.n_num_max_att; i++) {
		split_att[i] = malloc(strlen((char*)in_str));
	}
	int *vec_temp = calloc(PLC_INFO.n_num_max_att, sizeof(int*));
	
	int n_split = 0;
	int split_type;
	int vec_len_temp;
	uint8_t str_temp[strlen((char*)in_str)];
	strcpy((char*)str_temp,(char*)in_str);
	for(int j=0;j<*vec_len;j++) {
		vec_temp[j] = vec[j];
	}
	int* vec_temp2;
	
	vec_len_temp=*vec_len;
	
	split_str_plc(split_att, &n_split, &split_type, str_temp);
	
	if (split_type == 2) {
		strcpy((char*)att_list[*u_temp],(char*)split_att[0]);
		for(int j=0;j<vec_len_temp;j++) {
			plc_mat[*u_temp][j] = vec[j];
		}
		(*u_temp)++;

	} else if (split_type == 0) {
	//Case OR. Pass same vec and veclen
		for(int x=0;x<n_split;x++) {
			str_plc_to_vec(plc_mat,att_list,vec_temp,&vec_len_temp,u_temp,t_temp,split_att[x],PLC_INFO);
			if(*t_temp > vec_len_temp) {
				for (int i=vec_len_temp;i<*t_temp;i++) {
					vec_temp[i]=0;
				}
				vec_len_temp = *t_temp;
			}
		}
	} else if (split_type == 1) {
		vec_len_temp += n_split -1;
		vec_temp2 = (int*)malloc((n_split-1) * sizeof(int));
		for (int k=0;k<n_split-1;k++) {
			vec_temp2[k] = 1;
		}
		
		if (vec_len_temp > *t_temp) {
			*t_temp = vec_len_temp;
		}
		
		for(int x=0;x<n_split;x++) {
			if (x == 1) {
				for (int j=0;j<vec_len_temp-n_split+1;j++) {
					vec_temp[j] = 0;
				}
			}
			if (x>=1) {
				for (int k=0;k<n_split-1;k++) {
					if (k == x-1) {
						vec_temp2[k] = 1;
					} else {
						vec_temp2[k] = 0;
					}
				}	
			}
			for (int k=0;k<n_split-1;k++) {
				vec_temp[k+vec_len_temp-n_split+1] = vec_temp2[k];
			}	
			str_plc_to_vec(plc_mat,att_list,vec_temp,&vec_len_temp,u_temp,t_temp,split_att[x],PLC_INFO);
		}
		free(vec_temp2);
	} else {
	//Only 3 split type could be returned.
		printf("ERROR: Split type error\n");
	}
	
	for(int i=0; i<PLC_INFO.n_num_max_att; i++) {
		free(split_att[i]);
	}
	free(split_att);
	free(vec_temp);
	return 0;
}

int str_plc_to_mat(int **plc_mat, uint8_t **att_list, int* u, int* t, uint8_t* in_str, plc_info_t PLC_INFO) {
	int u_temp = 0;
	int t_temp = 1;
	int vec_len = 1;
	int *vec = calloc(PLC_INFO.n_num_max_att, sizeof(int*));
	vec[0]=1;
	
	str_plc_to_vec(plc_mat,att_list,vec,&vec_len,&u_temp,&t_temp,in_str,PLC_INFO);
	
	*u=u_temp;
	*t=t_temp;
	
	free(vec);
	
	return 0;
}

/* ---------------------------------------Det/Inv Matrix--------------------------------------- */
float det_mat(float **inmat, int size) {
	if (size==1) {
		return inmat[0][0];
	} else {
		float **temp = malloc((size-1) * sizeof(float*));
		for(int i=0; i<size-1; i++) {
			temp[i] = calloc(size-1, sizeof(float*));
		}
		float det = 0;
		int m,n;
		
		for(int k = 0; k<size; k++) {
			if (inmat[0][k] != 0) {
			//Skip element that is 0 because anything time 0 is 0
				for(int i = 0; i<size-1; i++) {
					for(int j = 0; j<size-1; j++) {
						m = i+1;
						if (k == size){
							break;
						} else if (j>=k) {
							n=j+1;
						} else {
							n=j;
						}
						temp[i][j] = inmat[m][n];
						//printf("temp[i][j]: %f  ",temp[i][j]);
					}
					
				}
				if (k%2==0){
					det += inmat[0][k] * det_mat(temp,size-1);	
				} else {
					det -= inmat[0][k] * det_mat(temp,size-1);
				}
				//printf("    det: %f\n",det);
			}
		}
		for(int i=0; i<size-1; i++) {
			free(temp[i]);
		}
		free(temp);
		return det;
	}
}

int inv_mat(float **outmat, float **inmat, int size) {
/* Required det(inmat)!=0 */
	float temp,det;
	
	// Create Identity matrix
	for(int i = 0; i<size; i++) {
		for(int j = 0; j<size; j++) {
			if(i==j) {
				outmat[i][j] = 1;
			} else {
				outmat[i][j] = 0;
			}
		}
	}
	
	// Check det
	det = det_mat(inmat, size);
	if((int)det == 0) {
		printf("Matrix is singular\n");
		return -1;
	} else {
		// Make U matrix from inmat
		for(int k = 0; k<size; k++) {
			if ((int)inmat[k][k] == 0) {
				for(int i = k+1; i<size; i++) {
					if ((int)inmat[i][k]!= 0) {
						for(int j = 0; j<size; j++) {
							temp = inmat[k][j];
							inmat[k][j] = inmat[i][j];
							inmat[i][j] = temp;
							temp = outmat[k][j];
							outmat[k][j] = outmat[i][j];
							outmat[i][j] = temp;
						}
						break;
					}
				}
			}
			
			temp = inmat[k][k];
			for(int j = 0; j<size; j++) {
				inmat[k][j] /= temp;
				outmat[k][j] /= temp;
			}
			
			for(int i = k+1; i<size; i++) {
				temp = inmat[i][k];
				for(int j = 0; j<size; j++) {
					inmat[i][j] -= temp * (inmat[k][j]);
					outmat[i][j] -= temp * (outmat[k][j]);
				}
			}
		}
		
		// Make I matrix from U matrix
		for(int i = size-2; i>=0; i--) {
			for(int j = size-1; j>i; j--) {
				temp = inmat[i][j];
				for(int k = 0; k<size; k++) {
					inmat[i][k] -= temp * (inmat[j][k]);
					outmat[i][k] -= temp * (outmat[j][k]);
				}
			}
		}
		return 0;
	}
}

/* ---------------------------------------Number Attribute--------------------------------------- */
void int2bin(uint8_t* binary, int integer, int n) {
	for (int i=0;i<n;i++)   
		binary[i] = (integer & (int)1<<(n-i-1)) ? '1' : '0';
	binary[n]='\0';
}

int plc_2_plcnum (uint8_t* plcnum, int* n_num_plc, uint8_t* in_str) {
	uint8_t str[strlen((char*)in_str)];
	strcpy((char*)str,(char*)in_str);
	uint8_t *pos_ptr;
	int symb_pos;
	int symb_case = 5;//0 is ==, 1 is >=, 2 is >, 3 is <=, 4 is <
	uint8_t num_str[ATT_NUM_BIT/3+2]; //log2(10)~3, +1 for ceil, +1 for '0'
	int num;
	uint8_t bits[ATT_NUM_BIT+1],stars[ATT_NUM_BIT+1],temp_stars[ATT_NUM_BIT+1];
	uint8_t last_bit='2';
	int skippable_bit,op_brack_cnt;
	
	for (int i=0;i<ATT_NUM_BIT;i++) {
		stars[i]='*';
	}
	stars[ATT_NUM_BIT]='\0';
	
	pos_ptr = (uint8_t*)strchr((char*)str,'>');
	if(pos_ptr != NULL) {
		symb_pos = pos_ptr - str;
		if(str[symb_pos+1]=='=') {
			symb_case=1; //case >=
		} else {
			symb_case=2; //case >
		}
	} else {
		pos_ptr = (uint8_t*)strchr((char*)str,'<');
		if(pos_ptr != NULL) {
			symb_pos = pos_ptr - str;
			if(str[symb_pos+1]=='=') {
				symb_case=3; //case <=
			} else {
				symb_case=4; //case <
			}
		} else {
			pos_ptr = (uint8_t*)strchr((char*)str,'=');
			if(pos_ptr != NULL) {
				symb_pos = pos_ptr - str;
				if(str[symb_pos+1]=='=') {
					symb_case=0; //case ==
				}
			} else {
			//Case normal attribute no number
				(*n_num_plc)=0;
				return 0;
			}
		}
	}
	
	uint8_t *att_pre= malloc(symb_pos+2);
	strncpy((char*)att_pre,(char*)str,symb_pos);
	att_pre[symb_pos]=':';
	att_pre[symb_pos+1]='\0';
		
	if (symb_case==2 || symb_case==4) {
		strcpy((char*)num_str,(char*)str+symb_pos+1);
	} else {
		strcpy((char*)num_str,(char*)str+symb_pos+2);
	}
	//printf("att_pre: %s num_str: %s\n",att_pre,num_str);
	
	num = (int) strtol((char*)num_str, (char **)NULL, 10);
	if (symb_case==2) {
		num++;
	} else if (symb_case==4) {
		num--;
	}
	//printf("num: %d\n",num);
	int2bin(bits,num,ATT_NUM_BIT);
	//printf("bits: %s\n",bits);
	
	strcpy((char*)plcnum,"");
	
	if(symb_case == 0) {
		(*n_num_plc) = ATT_NUM_BIT;
		for (int i=0;i<ATT_NUM_BIT;i++) {
			strcpy((char*)temp_stars,(char*)stars);
			temp_stars[i]=bits[i];
			strcat((char*)plcnum,(char*)att_pre);
			strcat((char*)plcnum,(char*)temp_stars);
			
			if (i!=ATT_NUM_BIT-1) {
				strcat((char*)plcnum,ABE_PLC_AND);
			}
		}
	} else {
		skippable_bit=0;
		op_brack_cnt=0;
		if(symb_case==1 || symb_case==2) {
		//Case >=,>
			for (int i=0;i<ATT_NUM_BIT;i++) {
				if (bits[ATT_NUM_BIT-i-1]!='0') {
					skippable_bit=i;
					break;
				}
			}
			(*n_num_plc) = ATT_NUM_BIT-skippable_bit;
			
			for (int i=0;i<ATT_NUM_BIT-skippable_bit;i++) {
				if(bits[i]=='0') {
					if(bits[i]!=last_bit && i!=0 && i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,"(");
						op_brack_cnt++;
					}
					
					strcpy((char*)temp_stars,(char*)stars);
					temp_stars[i]='1';
					strcat((char*)plcnum,(char*)att_pre);
					strcat((char*)plcnum,(char*)temp_stars);
					
					if (i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,ABE_PLC_OR);
					}
					
					last_bit = '0';
				} else {
					if(bits[i]!=last_bit && i!=0 && i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,"(");
						op_brack_cnt++;
					}
					
					strcpy((char*)temp_stars,(char*)stars);
					temp_stars[i]='1';
					strcat((char*)plcnum,(char*)att_pre);
					strcat((char*)plcnum,(char*)temp_stars);
					if (i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,ABE_PLC_AND);
					}
					last_bit = '1';
				}
				
				//printf("plcnum loop %d: %s\n",i,plcnum);
				if (i==ATT_NUM_BIT-skippable_bit-1) {
					for (int j=0;j<op_brack_cnt;j++) {
						strcat((char*)plcnum,")");
					}
				}
				
			}
		} else if(symb_case==3 || symb_case==4){
		//Case <=,<
			for (int i=0;i<ATT_NUM_BIT;i++) {
				if (bits[ATT_NUM_BIT-i-1]!='1') {
					skippable_bit=i;
					break;
				}
			}
			(*n_num_plc) = ATT_NUM_BIT-skippable_bit;
			
			for (int i=0;i<ATT_NUM_BIT-skippable_bit;i++) {
				if(bits[i]=='0') {
					if(bits[i]!=last_bit && i!=0 && i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,"(");
						op_brack_cnt++;
					}
					
					strcpy((char*)temp_stars,(char*)stars);
					temp_stars[i]='0';
					strcat((char*)plcnum,(char*)att_pre);
					strcat((char*)plcnum,(char*)temp_stars);
					
					if (i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,ABE_PLC_AND);
					}
					
					last_bit = '0';
				} else {
					if(bits[i]!=last_bit && i!=0 && i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,"(");
						op_brack_cnt++;
					}
					
					strcpy((char*)temp_stars,(char*)stars);
					temp_stars[i]='0';
					strcat((char*)plcnum,(char*)att_pre);
					strcat((char*)plcnum,(char*)temp_stars);
					if (i!=ATT_NUM_BIT-skippable_bit-1) {
						strcat((char*)plcnum,ABE_PLC_OR);
					}
					last_bit = '1';
				}
				
				//printf("plcnum loop %d: %s\n",i,plcnum);
				if (i==ATT_NUM_BIT-skippable_bit-1) {
					for (int j=0;j<op_brack_cnt;j++) {
						strcat((char*)plcnum,")");
					}
				}
			}
		}
	}
	free(att_pre);
	return 0;
}

int plc_all_2_plcnum (uint8_t* out_str, uint8_t* in_str, plc_info_t PLC_INFO) {
	uint8_t **split_att = malloc(PLC_INFO.n_max_split * sizeof(uint8_t *));
	for(int i=0; i<PLC_INFO.n_max_split; i++) {
		split_att[i] = malloc(strlen((char*)in_str));
	}
	int n_split = 0;
	int split_type;
	uint8_t str_temp[strlen((char*)in_str)];
	strcpy((char*)str_temp,(char*)in_str);
	int num;
	uint8_t *temp = malloc(PLC_INFO.plc_num_str_size);
	uint8_t *out_temp = malloc(PLC_INFO.plc_num_str_size);
	
	split_str_plc(split_att, &n_split, &split_type, str_temp);
	
	if (split_type == 2) {
		plc_2_plcnum(temp, &num, split_att[0]);
		if(num==0) {
			strcpy((char*)out_temp,(char*)split_att[0]);
		} else {
			strcpy((char*)out_temp,"");
			strcat((char*)out_temp,"(");
			strcat((char*)out_temp,(char*)temp);
			strcat((char*)out_temp,")");
		}
	} else if (split_type == 0) {
	//Case OR
		strcpy((char*)out_temp,"");
		strcat((char*)out_temp,"(");
		for (int i=0;i<n_split;i++) {
			plc_all_2_plcnum(temp, split_att[i], PLC_INFO);
			strcat((char*)out_temp,(char*)temp);
			if(i==n_split-1) {
				strcat((char*)out_temp,")");
			} else {
				strcat((char*)out_temp,ABE_PLC_OR);
			}
		}
	} else if (split_type == 1) {
	//Case AND
		strcpy((char*)out_temp,"");
		strcat((char*)out_temp,"(");
		for (int i=0;i<n_split;i++) {
			plc_all_2_plcnum(temp, split_att[i], PLC_INFO);
			strcat((char*)out_temp,(char*)temp);
			if(i==n_split-1) {
				strcat((char*)out_temp,")");
			} else {
				strcat((char*)out_temp,ABE_PLC_AND);
			}
		}
	}
	strcpy((char*)out_str,(char*)out_temp);
	
	for (int i = 0; i < PLC_INFO.n_max_split; i++) {
		free(split_att[i]);
	}
	free(split_att);
	free(out_temp);
	free(temp);
	return 0;
}


int att_2_attnum(uint8_t **attnum, int* n_num_att, uint8_t* in_str, int max_att_len) {
	uint8_t str[strlen((char*)in_str)];
	strcpy((char*)str,(char*)in_str);
	uint8_t *pos_ptr;
	int colon_pos;
	uint8_t *att_pre = malloc(max_att_len);
	uint8_t num_str[ATT_NUM_BIT/3+2]; //log2(10)~3, +1 for ceil, +1 for '0'
	int num;
	uint8_t bits[ATT_NUM_BIT+1],stars[ATT_NUM_BIT+1],temp_stars[ATT_NUM_BIT+1];
	
	for (int i=0;i<ATT_NUM_BIT;i++) {
		stars[i]='*';
	}
	stars[ATT_NUM_BIT]='\0';
	
	pos_ptr = (uint8_t*)strchr((char*)str,':');
	colon_pos = (pos_ptr == NULL ? -1 : pos_ptr - str);
	
	if(colon_pos == -1) {
		(*n_num_att) = 0;
	} else {
		(*n_num_att) = ATT_NUM_BIT;
		strncpy((char*)att_pre,(char*)str,colon_pos+1);
		att_pre[colon_pos+1]='\0';
		strcpy((char*)num_str,(char*)str+colon_pos+1);
		//printf("att_pre: %s num_str: %s\n",att_pre,num_str);
		num = (int) strtol((char*)num_str, (char **)NULL, 10);
		//printf("num: %d\n",num);
		int2bin(bits,num,ATT_NUM_BIT);
		//printf("bits: %s\n",bits);
		
		for (int i=0;i<ATT_NUM_BIT;i++) {
			strcpy((char*)temp_stars,(char*)stars);
			temp_stars[i]=bits[i];
			strcpy((char*)attnum[i],(char*)att_pre);
			strcat((char*)attnum[i],(char*)temp_stars);
		}
		
	}
	
	free(att_pre);
	
	return 0;
}

void user_att_2_attnum(uint8_t **user_attnum, uint8_t **user_att,int n_att, int max_att_len) {
	uint8_t **attnum = malloc(ATT_NUM_BIT * sizeof(uint8_t *));
	for(int i=0; i<ATT_NUM_BIT; i++) {
		attnum[i] = malloc(max_att_len);
	}
	int attnum_chk = 0;
	int k=0;
	for (int i=0;i<n_att;i++) {
		att_2_attnum(attnum,&attnum_chk,user_att[i], max_att_len);
		//printf("%d %d\n",i,attnum_chk);
		if(attnum_chk!=0) {
			for(int j=0;j<ATT_NUM_BIT;j++) {
				strcpy((char*)user_attnum[k+j],(char*)attnum[j]);
			}
			k+=ATT_NUM_BIT;
		} else {
			strcpy((char*)user_attnum[k],(char*)user_att[i]);
			k++;
		}
	}
	
	for(int i=0; i<ATT_NUM_BIT; i++) {
		free(attnum[i]);
	}
	free(attnum);
}

/* ---------------------------------------MSG ENC DEC--------------------------------------- */
int aes_kdf_enc(uint8_t *out, int *out_len, uint8_t *in, int in_len, gt_t gt) {
/* Apply key derivation function to gt and the result as the AES key to encrypt message "in" */
	int result = RLC_OK, key_len = AES_BYTE_LEN;
	uint8_t key[AES_BYTE_LEN], iv[AES_BYTE_LEN] = { 0 };
	uint8_t bin[12 * RLC_FP_BYTES];

	RLC_TRY {
		gt_write_bin(bin, sizeof(bin), gt, 0);
		md_kdf(key, key_len, bin, sizeof(bin));
		
		if (bc_aes_cbc_enc(out, out_len, in, in_len, key, key_len, iv) != RLC_OK) {
			result = RLC_ERR;
		} else {
			result = RLC_OK;
		}
	}
	RLC_CATCH_ANY {
		result = RLC_ERR;
	}	
	
	return result;
}

int aes_kdf_dec(uint8_t *out, int *out_len, uint8_t *in, int in_len, gt_t gt) {
/* Apply key derivation function to gt and the result as the AES key to decrypt message "in" */
	int result = RLC_OK, key_len = AES_BYTE_LEN;
	uint8_t key[AES_BYTE_LEN], iv[AES_BYTE_LEN] = { 0 };
	uint8_t bin[12 * RLC_FP_BYTES];

	RLC_TRY {
		gt_write_bin(bin, sizeof(bin), gt, 0);
		md_kdf(key, key_len, bin, sizeof(bin));
		
		if (bc_aes_cbc_dec(out, out_len, in, in_len, key, key_len, iv) != RLC_OK) {
			result = RLC_ERR;
		} else {
			result = RLC_OK;
		}
	}
	RLC_CATCH_ANY {
		result = RLC_ERR;
	}	
	
	return result;
}
