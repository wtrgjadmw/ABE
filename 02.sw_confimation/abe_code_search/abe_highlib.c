#include <stdio.h>
#include <abe_highlib.h>

/* ---------------------------------------Highlib Option1--------------------------------------- */
int h1_system_setup() {
	//printf("System Setup+++++++++++++\n");

	uint8_t pwd[BUFSIZ];
	//printf("Enter CA password: ");
	//get_stdin((char*)pwd);
	strcpy((char*)pwd,"capass");
	//printf("\n");
	mpk_t MPK;
	msk_t MSK;
	event(0,"h1_system_setup");
	abe_mk_set(&MPK,&MSK);
	event(1,"abe_mk_set_exit");
	abe_mpk_exp(ABE_MPK_FNAME, &MPK);
	event(1,"abe_mpk_exp");
	abe_msk_exp(ABE_MSK_FNAME, &MSK);
	event(1,"abe_msk_exp");
	// Free memory
	abe_mpk_free(&MPK);
	abe_msk_free(&MSK);
	event(1,"abe_mpk_msk_free");
	aes_kdf_file_enc(ABE_MSK_FNAME, pwd, F_REMOVE);
	event(1,"aes_kdf_file_enc_MSK");
	aes_kdf_file_enc(ABE_ATTDATA_FNAME, pwd, F_KEEP);
	event(1,"aes_kdf_file_enc_ATTDATA");
	event(3,"");
	return 0;
}

int h1_edit_att() {
	//printf("Edit Attribute+++++++++++++\n");

	uint8_t pwd[BUFSIZ];

	//printf("Enter CA password: ");
	//get_stdin((char*)pwd);
	strcpy((char*)pwd,"capass");
	//printf("\n");
	event(0,"h1_edit_att");
	char fname[strlen(ABE_ATTDATA_FNAME)+5];

	sprintf (fname, "%s.enc", ABE_ATTDATA_FNAME);
	event(1,"chg_filename");
	if(aes_kdf_file_dec(fname, pwd, F_REMOVE) == RLC_ERR) {
		printf("Wrong CA's password or error\n");
		return 1;
	}
	event(1,"aes_kdf_file_dec");

	//uint8_t s[BUFSIZ];
	//printf("Press Enter to finish editing attribute database.");
	//get_stdin((char*)s);
	//event(1,"wait_time");
	aes_kdf_file_enc(ABE_ATTDATA_FNAME, pwd, F_KEEP);
	event(1,"aes_kdf_file_enc");
	event(3,"");
	return 0;
}

int h1_user_regis() {
	//printf("User Registration+++++++++++++\n");

	uint8_t name[BUFSIZ];
	//printf("Please enter your name: ");
	//get_stdin((char*)name);
	strcpy((char*)name,"anawin");
	//printf("\n");

	uint8_t pwd[BUFSIZ];
	//printf("Please enter your password: ");
	//get_stdin((char*)pwd);
	strcpy((char*)pwd,"anawin");
	//printf("\n");

	event(0,"h1_user_regis");
	uint8_t kdf_pwd[KDF_LEN];
	md_kdf(kdf_pwd, KDF_LEN, pwd, strlen((char*)pwd));
	event(1,"md_kdf");
	uint8_t kdf_pwd_hex[KDF_LEN*2+1] = { '0' };
	bin2hex(kdf_pwd_hex , kdf_pwd, KDF_LEN);
	event(1,"bin2hex");
	FILE *inFile;
	inFile = fopen(ABE_REGIS_FNAME, "r+");          // Open the file
	if(inFile == NULL) {
		inFile = fopen(ABE_REGIS_FNAME, "w");          // Open the file
	} else {
		fseek(inFile, 0, SEEK_END);
		fwrite("\n",1, 1,inFile);
	}

	fwrite(name,strlen((char*)name), 1,inFile);
	fwrite(",pass=",6, 1,inFile);
	fwrite(kdf_pwd_hex,KDF_LEN*2, 1,inFile);

	fclose(inFile);
	event(1,"write_to_file");
	event(3,"");
	return 0;
}

int h1_encryption() {
	//printf("Encryption+++++++++++++\n");

	// User input
	uint8_t user_input_plc[BUFSIZ];
	//printf("Please enter policy for encryption: ");
	//get_stdin((char*)user_input_plc);
	strcpy((char*)user_input_plc,"A AND C AND F==10");
	//printf("\n");

	char fname[BUFSIZ];
	//printf("Please enter file name: ");
	//get_stdin(fname);
	strcpy((char*)fname,"test.png");
	//printf("\n");

	int option;
	//printf("Do you want the file to be kept after encrypted? (0 for remove and 1 for keep): ");
	//scanf("%d",&option);
	option = 1;
	//printf("\n");

	char fname_o[strlen((char*)fname)+4];
	sprintf(fname_o, "%s.enc", fname);

	event(0,"h1_encryption");
	// Reading file
	FILE *inFile;
	int filelen;

	inFile = fopen(fname, "r");          // Open the file
	if(inFile == NULL) {
		printf("Error cannot find the file specified\n");
		return RLC_ERR;
	}
	fseek(inFile, 0, SEEK_END);          // Jump to the end of the file
	filelen = ftell(inFile);             // Get the current byte offset in the file
	rewind(inFile);                      // Jump back to the beginning of the file

	uint8_t *msg = malloc(filelen * sizeof(char)); // Enough memory for the file
	fread((char*)msg, filelen, 1, inFile); // Read in the entire file
	fclose(inFile);
	event(1,"read_target_file");

	// Processing policy
	plc_info_t PLC_INFO;
	plc_string_info_init(&PLC_INFO, user_input_plc);
	plc_string_info(&PLC_INFO, user_input_plc);

	//printf("The number of attributes corresponds to the input policy is: %d\n",PLC_INFO.n_att);

	uint8_t *plcnum = malloc(PLC_INFO.plc_num_str_size);
	uint8_t *plc = malloc(PLC_INFO.n_num_max_att * (2*ATT_HASH_LEN) + (PLC_INFO.n_num_max_att-1)*(strlen(ABE_PLC_AND)+2));
	event(1,"processing_policy");
	// -Converting to number policy
	plc_all_2_plcnum(plcnum, user_input_plc, PLC_INFO);
	event(1,"num_policy");

	// -Re-inspect the policy
	plc_string_info_init(&PLC_INFO, plcnum);
	plc_string_info(&PLC_INFO, plcnum);
	event(1,"processing_policy");
	// -Hash each attribute in the policy
	plc_hash(plc,plcnum,PLC_INFO);
	event(1,"plc_hash");

	// Encryption
	abe_ct_t CT;
	mpk_t MPK;
	abe_mpk_imp(&MPK, ABE_MPK_FNAME);
	event(1,"abe_mpk_imp");
	abe_ct_set(&CT, MPK, plc, msg, filelen, PLC_INFO);
	event(1,"abe_ct_set_exit");
	abe_ct_exp(fname_o,&CT);
	event(1,"abe_ct_exp");


	if (option == F_REMOVE) {
		remove(fname);
	}

	// Free memory
	abe_ct_free(&CT);
	abe_mpk_free(&MPK);
	free(plcnum);
	free(plc);
	free(msg);
	event(1,"free");
	event(3,"");
	return 0;
}

int h1_decryption() {
	//printf("Decryption+++++++++++++\n");

	// User input
	//char input_buf[BUFSIZ];
	//printf("Please enter CA password: ");
	//get_stdin(input_buf);

	uint8_t *ca_pwd = malloc(7);
	//strcpy((char*)ca_pwd,input_buf);
	strcpy((char*)ca_pwd,"capass");
	//printf("\n");

	//printf("Please enter your username: ");
	//get_stdin(input_buf);

	uint8_t *username = malloc(7);
	//strcpy((char*)username,input_buf);
	strcpy((char*)username,"anawin");
	//printf("\n");

	//printf("Please enter your password: ");
	//get_stdin(input_buf);

	uint8_t *user_pass = malloc(7);
	//strcpy((char*)user_pass,input_buf);
	strcpy((char*)user_pass,"anawin");
	//printf("\n");

	event(0,"h1_decryption");
	// Check user from the registration file
	int result;
	if(check_user_regis(&result, username, user_pass) == RLC_ERR) {
		free(ca_pwd);
		free(username);
		free(user_pass);
		return 1;
	}
	event(1,"check_user_regis");

	// Decrypt the MSK that were encrypted with CA's password
	char msk_fname[50];
	strcpy(msk_fname,ABE_MSK_FNAME);
	strcat(msk_fname,".enc");
	if(aes_kdf_file_dec(msk_fname, ca_pwd, F_KEEP) == RLC_ERR) {
		printf("Wrong CA's password or error\n");
		free(ca_pwd);
		free(username);
		free(user_pass);
		return 1;
	}
	msk_t MSK;
	event(1,"aes_kdf_file_dec");
	abe_msk_imp(&MSK, ABE_MSK_FNAME);
	event(1,"abe_msk_imp");
	remove(ABE_MSK_FNAME);

	// Decrypt attribute database that were encrypted with CA's password
	char attdata_fname[50];
	strcpy(attdata_fname,ABE_ATTDATA_FNAME);
	strcat(attdata_fname,".enc");
	if(aes_kdf_file_dec(attdata_fname, ca_pwd, F_KEEP) == RLC_ERR) {
		printf("Wrong CA's password or error\n");
		free(ca_pwd);
		free(username);
		free(user_pass);
		return 1;
	}
	event(1,"aes_kdf_file_dec");

	// Reading attribute data of user
	int user_n_att;
	char attdata[500];
	if(get_user_att_data(&result, attdata, &user_n_att, username) == RLC_ERR) {
		free(ca_pwd);
		free(username);
		free(user_pass);
		return 1;
	}
	event(1,"get_user_att_data");

	// Convert attribute data of user into array
	uint8_t **user_att;
	user_att = malloc(user_n_att * sizeof(uint8_t *));
	for(int i=0; i<user_n_att; i++) {
		user_att[i] = malloc(strlen(attdata));
	}
	user_att_data_to_array(user_att, user_n_att, attdata);
	event(1,"user_att_data_to_array");

	// Convert user attributes into number attributes
	int n_attnum = user_n_att;
	int max_att_len = 0;
	user_att_assess_for_attnum(&max_att_len, &n_attnum, user_att);
	uint8_t **user_attnum = malloc(n_attnum * sizeof(uint8_t *));
	for(int i=0; i<n_attnum; i++) {
		user_attnum[i] = malloc(max_att_len);
	}
	user_att_2_attnum(user_attnum,user_att,user_n_att,max_att_len);
	event(1,"user_att_2_attnum");

	// Set up user key
	abe_key_t KEY;
	mpk_t MPK;
	abe_mpk_imp(&MPK, ABE_MPK_FNAME);
	event(1,"abe_mpk_imp");
	abe_key_set(&KEY,MPK,MSK,user_attnum,n_attnum);
	event(1,"abe_key_set_exit");

	// Set up CT
	//printf("Please enter filename to be decrypted: ");
	//get_stdin(input_buf);

	char *dec_fname = malloc(30);
	//strcpy(dec_fname,input_buf);
	strcpy(dec_fname,"test.png.enc");
	//printf("\n");
	event(1,"dec_fname");

	abe_ct_t CT;
	if(abe_ct_imp(&CT,dec_fname) == RLC_ERR) {
		return 1;
	}
	event(1,"abe_ct_imp");

	// Decrypt CT with KEY
	int dec_len = CT.enc_len + 1;
	uint8_t *dec_msg = malloc(dec_len+1);

	gt_t output;
	gt_null(output);
	gt_new(output);
	event(1,"decrypt_var");
	abe_decrypt(dec_msg, &dec_len, output, CT, KEY);
	event(1,"abe_decrypt_exit");

	// Write file with decrypted content
	char* pos_ptr;
	char fname_o[strlen((char*)dec_fname)+1];
	pos_ptr = strstr(dec_fname,".enc");
	strncpy(fname_o,dec_fname,pos_ptr-dec_fname);
	fname_o[pos_ptr-dec_fname]='\0';

	FILE *fp;
	fp = fopen(fname_o, "w");
	fwrite(dec_msg,dec_len,1,fp);
	fclose(fp);

	//remove(dec_fname);
	event(1,"fwrite_decrypted_file");

	// Free malloc variables
	free(ca_pwd);
	free(username);
	free(user_pass);
	free(dec_msg);
	free(dec_fname);
	for(int i=0; i<user_n_att; i++) {
		free(user_att[i]);
	}
	free(user_att);
	for(int i=0; i<n_attnum; i++) {
		free(user_attnum[i]);
	}
	free(user_attnum);
	event(1,"free");
	event(3,"");
	return 0;
}

/* ---------------------------------------Highlib Option2--------------------------------------- */
int h2_system_setup() {
	//printf("System Setup+++++++++++++\n");

	// User input
	uint8_t pwd[BUFSIZ];
	//printf("Enter CA password: ");
	//get_stdin((char*)pwd);
	strcpy((char*)pwd,"capass");
	//printf("\n");

	event(0,"h2_system_setup");
	// Set up MPK,MSK,MPK2,MSK2 and export to file
	mpk_t MPK,MPK2;
	msk_t MSK,MSK2;

	// Set up MPK,MSK,MPK2,MSK2 and export to file
	abe_mk_set(&MPK,&MSK);
	abe_mk_set(&MPK2,&MSK2);
	event(1,"abe_mpk_msk_set");

	abe_mpk_exp(ABE_MPK_FNAME, &MPK);
	abe_msk_exp(ABE_MSK_FNAME, &MSK);

	abe_mpk_exp(ABE_MPK2_FNAME, &MPK2);
	abe_msk_exp(ABE_MSK2_FNAME, &MSK2);

	event(1,"abe_mpk_msk_exp");

	// Encrypt MSK2 file and AttData file with policy "Member"
	abe_file_enc(ABE_MSK2_FNAME, (uint8_t*)"Member", MPK, F_REMOVE);
	abe_file_enc(ABE_ATTDATA_FNAME, (uint8_t*)"Member", MPK, F_KEEP);
	event(1,"abe_file_enc");

	// Encrypt MSK and MPK with CA's password
	aes_kdf_file_enc(ABE_MSK_FNAME, pwd, F_REMOVE);
	aes_kdf_file_enc(ABE_MPK_FNAME, pwd, F_REMOVE);
	event(1,"aes_kdf_file_enc");

	// Free memory
	abe_mpk_free(&MPK);
	abe_msk_free(&MSK);
	abe_mpk_free(&MPK2);
	abe_msk_free(&MSK2);

	event(1,"free");
	event(3,"");

	return 0;
}

int h2_user_regis() {
	//printf("User Registration+++++++++++++\n");

	// User input
	//char input_buf[BUFSIZ];
	//printf("Please enter CA password: ");
	//get_stdin(input_buf);

	uint8_t *ca_pwd = malloc(7);
	//strcpy((char*)ca_pwd,input_buf);
	strcpy((char*)ca_pwd,"capass");
	//printf("\n");

	//printf("Please enter your name: ");
	//get_stdin(input_buf);
	uint8_t *name = malloc(7);
	//strcpy((char*)name,input_buf);
	strcpy((char*)name,"anawin");
	//printf("\n");

	//printf("Please enter your password: ");
	//get_stdin(input_buf);
	uint8_t *pwd = malloc(7);
	//strcpy((char*)pwd,input_buf);
	strcpy((char*)pwd,"anawin");
	//printf("\n");

	event(0,"h2_user_regis");
	uint8_t kdf_pwd[KDF_LEN];
	md_kdf(kdf_pwd, KDF_LEN, pwd, strlen((char*)pwd));
	event(1,"md_kdf");
	uint8_t kdf_pwd_hex[KDF_LEN*2+1] = { '0' };
	bin2hex(kdf_pwd_hex , kdf_pwd, KDF_LEN);
	event(1,"bin2hex");
	FILE *inFile;
	inFile = fopen(ABE_REGIS_FNAME, "r+");          // Open the file
	if(inFile == NULL) {
		inFile = fopen(ABE_REGIS_FNAME, "w");          // Open the file
	} else {
		fseek(inFile, 0, SEEK_END);
		fwrite("\n",1, 1,inFile);
	}

	fwrite(name,strlen((char*)name), 1,inFile);
	fwrite(",pass=",6, 1,inFile);
	fwrite(kdf_pwd_hex,KDF_LEN*2, 1,inFile);

	fclose(inFile);
	event(1,"write_to_file");

	// Decrypt MSK and MPK to use
	char fname[30];
	sprintf (fname, "%s.enc", ABE_MSK_FNAME);
	aes_kdf_file_dec(fname, ca_pwd, F_KEEP);
	event(1,"aes_kdf_file_dec");
	msk_t MSK;
	abe_msk_imp(&MSK, ABE_MSK_FNAME);
	remove(ABE_MSK_FNAME);
	event(1,"abe_msk_imp");

	strcpy(fname,"");
	sprintf (fname, "%s.enc", ABE_MPK_FNAME);
	aes_kdf_file_dec(fname, ca_pwd, F_KEEP);
	event(1,"aes_kdf_file_dec");
	mpk_t MPK;
	abe_mpk_imp(&MPK, ABE_MPK_FNAME);
	event(1,"abe_mpk_imp");
	remove(ABE_MPK_FNAME);

	// Generate key with Member as attribute
	abe_key_t KEY;
	uint8_t **user_attnum = malloc(1 * sizeof(uint8_t *));
	user_attnum[0] = malloc(7);
	strcpy((char*)user_attnum[0],"Member");
	int n_attnum = 1;
	abe_key_set(&KEY,MPK,MSK,user_attnum,n_attnum);
	event(1,"abe_key_set_exit");

	char *fname_o = malloc(strlen((char*)name)+9);
	sprintf(fname_o, "%skey.txt", name);
	abe_key_exp(fname_o, &KEY);
	event(1,"abe_key_exp");
	aes_kdf_file_enc(fname_o, pwd, F_REMOVE);
	event(1,"aes_kdf_file_enc");

	// Free memory
	abe_mpk_free(&MPK);
	abe_msk_free(&MSK);
	abe_key_free(&KEY);
	free(fname_o);
	free(user_attnum[0]);
	free(user_attnum);
	free(pwd);
	free(name);
	free(ca_pwd);
	event(1,"free");
	event(3,"");
	return 0;
}

int h2_encryption() {
	//printf("Encryption+++++++++++++\n");

	uint8_t user_input_plc[BUFSIZ];
	//printf("Please enter policy for encryption: ");
	//get_stdin((char*)user_input_plc);
	strcpy((char*)user_input_plc,"A AND C AND F==10");
	//printf("\n");

	char fname[BUFSIZ];
	//printf("Please enter file name: ");
	//get_stdin(fname);
	strcpy((char*)fname,"test.png");
	//printf("\n");

	int option;
	//printf("Do you want the file to be kept after encrypted? (0 for remove and 1 for keep): ");
	//scanf("%d",&option);
	option = 1;
	//printf("\n");

	char fname_o[strlen((char*)fname)+4];
	sprintf(fname_o, "%s.enc", fname);

	event(0,"h2_encryption");
	// Reading file
	FILE *inFile;
	int filelen;

	inFile = fopen(fname, "r");          // Open the file
	if(inFile == NULL) {
		printf("Error cannot find the file specified\n");
		return RLC_ERR;
	}
	fseek(inFile, 0, SEEK_END);          // Jump to the end of the file
	filelen = ftell(inFile);             // Get the current byte offset in the file
	rewind(inFile);                      // Jump back to the beginning of the file

	uint8_t *msg = malloc(filelen * sizeof(char)); // Enough memory for the file
	fread((char*)msg, filelen, 1, inFile); // Read in the entire file
	fclose(inFile);
	event(1,"read_target_file");

	// Processing policy
	plc_info_t PLC_INFO;
	plc_string_info_init(&PLC_INFO, user_input_plc);
	plc_string_info(&PLC_INFO, user_input_plc);

	//printf("The number of attributes corresponds to the input policy is: %d\n",PLC_INFO.n_att);

	uint8_t *plcnum = malloc(PLC_INFO.plc_num_str_size);
	uint8_t *plc = malloc(PLC_INFO.n_num_max_att * (2*ATT_HASH_LEN) + (PLC_INFO.n_num_max_att-1)*(strlen(ABE_PLC_AND)+2));
	event(1,"processing_policy");
	// -Converting to number policy
	plc_all_2_plcnum(plcnum, user_input_plc, PLC_INFO);
	event(1,"num_policy");
	// -Re-inspect the policy
	plc_string_info_init(&PLC_INFO, plcnum);
	plc_string_info(&PLC_INFO, plcnum);
	event(1,"processing_policy");
	// -Hash each attribute in the policy
	plc_hash(plc,plcnum,PLC_INFO);
	event(1,"plc_hash");

	// Encryption
	abe_ct_t CT;
	mpk_t MPK2;
	abe_mpk_imp(&MPK2, ABE_MPK2_FNAME);
	event(1,"abe_mpk_imp");
	abe_ct_set(&CT, MPK2, plc, msg, filelen, PLC_INFO);
	event(1,"abe_ct_set_exit");
	abe_ct_exp(fname_o,&CT);
	event(1,"abe_ct_exp");

	if (option == F_REMOVE) {
		remove(fname);
	}

	// Free memory
	abe_ct_free(&CT);
	abe_mpk_free(&MPK2);
	free(plcnum);
	free(plc);
	free(msg);
	event(1,"free");
	event(3,"");
	return 0;
}

int h2_decryption() {
	//printf("Decryption+++++++++++++\n");

	// User input
	//char input_buf[BUFSIZ];
	//printf("Please enter your username: ");
	//get_stdin(input_buf);

	uint8_t *username = malloc(7);
	//strcpy((char*)username,input_buf);
	strcpy((char*)username,"anawin");
	//printf("\n");

	//printf("Please enter your password: ");
	//get_stdin(input_buf);

	uint8_t *user_pass = malloc(7);
	//strcpy((char*)user_pass,input_buf);
	strcpy((char*)user_pass,"anawin");

	event(0,"h1_decryption");
	// Check user from the registration file
	int result;
	if(check_user_regis(&result, username, user_pass) == RLC_ERR) {
		free(username);
		free(user_pass);
		return 1;
	}
	event(1,"check_user_regis");

	// Decrypt User ABE KEy
	abe_key_t user_abe_KEY;
	char fname_temp[40];
	sprintf (fname_temp, "%skey.txt.enc", username);
	aes_kdf_file_dec(fname_temp, user_pass, F_KEEP);
	event(1,"aes_kdf_file_dec");
	strcpy(fname_temp,"");
	sprintf (fname_temp, "%skey.txt", username);
	abe_key_imp(&user_abe_KEY,fname_temp);
	event(1,"abe_key_imp");
	remove(fname_temp);

	// Decrypt MSK2
	abe_ct_t msk2_CT;
	strcpy(fname_temp,"");
	sprintf (fname_temp, "%s.enc", ABE_MSK2_FNAME);
	abe_ct_imp(&msk2_CT,fname_temp);
	event(1,"abe_ct_imp_msk2_CT");

	int dec_len1 = msk2_CT.enc_len + 1;
	uint8_t *dec_msg1 = malloc(dec_len1+1);

	gt_t output;
	gt_null(output);
	gt_new(output);
	event(1,"decrypt_var");
	abe_decrypt(dec_msg1, &dec_len1, output, msk2_CT, user_abe_KEY);
	event(1,"abe_decrypt_exit");

	FILE *fp;
	fp = fopen(ABE_MSK2_FNAME, "w");
	fwrite(dec_msg1,dec_len1,1,fp);
	fclose(fp);
	event(1,"fwrite_dec_msg1");

	// Decrypt AttData
	abe_ct_t attdata_CT;
	strcpy(fname_temp,"");
	sprintf (fname_temp, "%s.enc", ABE_ATTDATA_FNAME);
	abe_ct_imp(&attdata_CT,fname_temp);
	event(1,"abe_ct_imp_attdata_CT");

	int dec_len2 = attdata_CT.enc_len + 1;
	uint8_t *dec_msg2 = malloc(dec_len2+1);
	event(1,"decrypt_var");
	abe_decrypt(dec_msg2, &dec_len2, output, attdata_CT, user_abe_KEY);
	event(1,"abe_decrypt_exit");

	fp = fopen(ABE_ATTDATA_FNAME, "w");
	fwrite(dec_msg2,dec_len2,1,fp);
	fclose(fp);
	event(1,"fwrite_dec_msg2");

	// Reading attribute data of user
	int user_n_att;
	char attdata[500];
	if(get_user_att_data(&result, attdata, &user_n_att, username) == RLC_ERR) {
		free(username);
		free(user_pass);
		return 1;
	}
	event(1,"get_user_att_data");

	// Convert attribute data of user into array
	uint8_t **user_att;
	user_att = malloc(user_n_att * sizeof(uint8_t *));
	for(int i=0; i<user_n_att; i++) {
		user_att[i] = malloc(strlen(attdata));
	}
	user_att_data_to_array(user_att, user_n_att, attdata);
	event(1,"user_att_data_to_array");

	// Convert user attributes into number attributes
	int n_attnum = user_n_att;
	int max_att_len = 0;
	user_att_assess_for_attnum(&max_att_len, &n_attnum, user_att);
	uint8_t **user_attnum = malloc(n_attnum * sizeof(uint8_t *));
	for(int i=0; i<n_attnum; i++) {
		user_attnum[i] = malloc(max_att_len);
	}
	user_att_2_attnum(user_attnum,user_att,user_n_att,max_att_len);
	event(1,"user_att_2_attnum");
	
	// Set up user ABE key
	abe_key_t KEY2;
	mpk_t MPK2;
	abe_mpk_imp(&MPK2, ABE_MPK2_FNAME);
	msk_t MSK2;
	abe_msk_imp(&MSK2, ABE_MSK2_FNAME);
	event(1,"abe_mpk_msk_imp");
	remove(ABE_MSK2_FNAME);

	abe_key_set(&KEY2,MPK2,MSK2,user_attnum,n_attnum);
	event(1,"abe_key_set_exit");
	// Set up CT
	//printf("Please enter filename to be decrypted: ");
	//get_stdin(input_buf);

	char *dec_fname = malloc(30);
	//strcpy(dec_fname,input_buf);
	strcpy(dec_fname,"test.png.enc");

	abe_ct_t CT;
	if(abe_ct_imp(&CT,dec_fname) == RLC_ERR) {
		return 1;
	}
	event(1,"abe_ct_imp");

	int dec_len = CT.enc_len + 1;
	uint8_t *dec_msg = malloc(dec_len+1);

	event(1,"decrypt_var");
	abe_decrypt(dec_msg, &dec_len, output, CT, KEY2);
	event(1,"abe_decrypt_exit");

	// Write file with decrypted content
	char* pos_ptr;
	char fname_o[strlen((char*)dec_fname)+1];
	pos_ptr = strstr(dec_fname,".enc");
	strncpy(fname_o,dec_fname,pos_ptr-dec_fname);
	fname_o[pos_ptr-dec_fname]='\0';

	fp = fopen(fname_o, "w");
	fwrite(dec_msg,dec_len,1,fp);

	fclose(fp);
	//remove(dec_fname);
	event(1,"fwrite_decrypted_file");
	// Free malloc variables
	free(username);
	free(user_pass);
	free(dec_msg);
	free(dec_fname);
	free(dec_msg1);
	free(dec_msg2);
	for(int i=0; i<user_n_att; i++) {
		free(user_att[i]);
	}
	free(user_att);
	for(int i=0; i<n_attnum; i++) {
		free(user_attnum[i]);
	}
	free(user_attnum);
	event(1,"free");
	event(3,"");
	return 0;
}

/* ---------------------------------------ABE Base Operation--------------------------------------- */
int system_setup() {
	mpk_t MPK;
	msk_t MSK;

	abe_mk_set(&MPK,&MSK);

	abe_mpk_exp(ABE_MPK_FNAME, &MPK);
	abe_msk_exp(ABE_MSK_FNAME, &MSK);

	// Free memory
	abe_mpk_free(&MPK);
	abe_msk_free(&MSK);

	return 0;
}

int user_encrypt() {
	uint8_t user_input_plc[]="(A AND B AND C) OR (D AND (E OR F>5) AND G) OR ((H OR J) AND K)";
	//"(att0 AND att1) OR (att2 AND att3 AND att4) OR (att5 AND att6 AND att9) OR (att7 AND att8)"
	uint8_t msg[]="Thrice the Brinded Cat Hath Mew'd";

	printf("Message is: ");
	printf("%s\n",msg);
	printf("Policy is: ");
	printf("%s\n",user_input_plc);

	plc_info_t PLC_INFO;
	plc_string_info_init(&PLC_INFO, user_input_plc);
	plc_string_info(&PLC_INFO, user_input_plc);

	printf("The number of attributes corresponds to the input policy is: %d\n",PLC_INFO.n_att);

	uint8_t *plcnum = malloc(PLC_INFO.plc_num_str_size);
	uint8_t *plc = malloc(PLC_INFO.n_num_max_att * (2*ATT_HASH_LEN) + (PLC_INFO.n_num_max_att-1)*(strlen(ABE_PLC_AND)+2));

	plc_all_2_plcnum(plcnum, user_input_plc, PLC_INFO);

	//printf("plcnum: %s\n",plcnum);
	plc_string_info_init(&PLC_INFO, plcnum);
	plc_string_info(&PLC_INFO, plcnum);

	plc_hash(plc,plcnum,PLC_INFO);
	//printf("plc: %s\n",plc);

	abe_ct_t CT;
	mpk_t MPK;
	abe_mpk_imp(&MPK, ABE_MPK_FNAME);

	abe_ct_set(&CT, MPK, plc, msg, strlen((char*)msg),PLC_INFO);
	//print_ct(CT);
	//gt_print(CT.C);

	abe_ct_exp(ABE_CT_FNAME,&CT);

	// Free memory
	abe_ct_free(&CT);
	abe_mpk_free(&MPK);
	free(plcnum);
	free(plc);

	return 0;
}

int user_key_gen() {
	int n_att = 7;
	//char temp[3];

	uint8_t **user_att = malloc(n_att * sizeof(uint8_t *));
	for(int i=0; i<n_att; i++) {
		user_att[i] = malloc(BUFSIZ);
		//strcpy((char*)user_att[i],"att");
		//snprintf(temp, 3, "%d", i ); // 3 for 2 digits + '\0'
		//strcat((char*)user_att[i],temp);
	}

	strcpy((char*)user_att[0],"A");
	strcpy((char*)user_att[1],"BB");
	strcpy((char*)user_att[2],"C");
	strcpy((char*)user_att[3],"D");
	strcpy((char*)user_att[4],"EE");
	strcpy((char*)user_att[5],"F:10");
	strcpy((char*)user_att[6],"G");
	//strcpy((char*)user_att[7],"H");
	//strcpy((char*)user_att[8],"I");

	int n_attnum = n_att;
	int max_att_len = 0;
	int att_len;
	uint8_t *pos_ptr;
	for(int i=0; i<n_att; i++) {
		pos_ptr = (uint8_t*)strchr((char*)user_att[i],':');
		if (pos_ptr == NULL) {
			att_len = strlen((char*)user_att[i]);
		} else {
			n_attnum += ATT_NUM_BIT - 1;
			att_len = pos_ptr - user_att[i] + ATT_NUM_BIT + 2;
		}

		if(att_len>max_att_len) {
			max_att_len = att_len;
		}
	}

	uint8_t **user_attnum = malloc(n_attnum * sizeof(uint8_t *));
	for(int i=0; i<n_attnum; i++) {
		user_attnum[i] = malloc(max_att_len);
	}

	user_att_2_attnum(user_attnum,user_att,n_att,max_att_len);

	for(int i=0; i<n_attnum; i++) {
		printf("user_attnum[%d]:%s\n",i,user_attnum[i]);
	}

	abe_key_t KEY;
	mpk_t MPK;
	abe_mpk_imp(&MPK, ABE_MPK_FNAME);
	msk_t MSK;
	abe_msk_imp(&MSK, ABE_MSK_FNAME);

	abe_key_set(&KEY,MPK,MSK,user_attnum,n_attnum);
	//print_key(KEY);

	abe_key_exp(ABE_KEY_FNAME, &KEY);

	// Free memory
	for(int i=0; i<n_att; i++) {
		free(user_att[i]);
	}
	for(int i=0; i<n_attnum; i++) {
		free(user_attnum[i]);
	}
	free(user_attnum);
	abe_key_free(&KEY);
	abe_mpk_free(&MPK);
	abe_msk_free(&MSK);

	return 0;
}

int user_decrypt() {
	abe_key_t KEY;
	abe_key_imp(&KEY, ABE_KEY_FNAME);

	abe_ct_t CT;
	abe_ct_imp(&CT,ABE_CT_FNAME);

	int dec_len = CT.enc_len + 1;
	uint8_t *dec_msg = malloc(dec_len+100);

	gt_t output;
	gt_null(output);
	gt_new(output);

	abe_decrypt(dec_msg, &dec_len, output, CT, KEY);

	printf("dec_msg: %s\n",dec_msg);
	//printf("output\n");
	//gt_print(output);

	// Free memory
	free(dec_msg);
	abe_key_free(&KEY);
	abe_ct_free(&CT);
	return 0;
}

/* ---------------------------------------Text File Enc/Dec--------------------------------------- */
int aes_kdf_file_enc(char *fname, uint8_t *pwd, int option) {
	char fname_o[strlen((char*)fname)+4];
	int result = RLC_OK, key_len = AES_BYTE_LEN;
	uint8_t key[2*AES_BYTE_LEN], iv[AES_BYTE_LEN] = { 0 };
	FILE *inFile,*outFile;
	char *buffer,*buffer_o;
	int filelen,filelen_o;

	RLC_TRY {
		md_kdf(key, 2*key_len, pwd, strlen((char*)pwd));

		inFile = fopen(fname, "r");          // Open the file
		if(inFile == NULL) {
			printf("Error cannot find the file specified\n");
			return RLC_ERR;
		}
		fseek(inFile, 0, SEEK_END);          // Jump to the end of the file
		filelen = ftell(inFile);             // Get the current byte offset in the file
		rewind(inFile);                      // Jump back to the beginning of the file

		buffer = (char *)malloc(filelen * sizeof(char)); // Enough memory for the file
		fread(buffer, filelen, 1, inFile); // Read in the entire file
		fclose(inFile);

		filelen_o = AES_BYTE_LEN*(filelen/AES_BYTE_LEN);
		if(filelen % AES_BYTE_LEN!=0) {
			filelen_o+=AES_BYTE_LEN;
		}

		buffer_o = (char *)malloc(filelen_o * sizeof(char) + RLC_MD_LEN);

		if (bc_aes_cbc_enc((uint8_t *)buffer_o, &filelen_o, (uint8_t *)buffer, filelen, key, key_len, iv) != RLC_OK) {
			result = RLC_ERR;
		} else {
			md_hmac((uint8_t *)buffer_o + filelen_o, (uint8_t *)buffer_o, filelen_o, key + key_len, key_len);
			filelen_o += RLC_MD_LEN;
			result = RLC_OK;
		}

		sprintf (fname_o, "%s.enc", fname);
		outFile = fopen(fname_o, "w");
		fwrite(buffer_o,filelen_o, 1,outFile);
		fclose(outFile);

		free(buffer);
		free(buffer_o);
	}
	RLC_CATCH_ANY {
		result = RLC_ERR;
	}

	if (option == F_REMOVE) {
		remove(fname);
	}

	return result;
}

int aes_kdf_file_dec(char *fname, uint8_t *pwd, int option) {
	char fname_o[strlen((char*)fname)+4],fname_o_ext[10],fname_o_temp[strlen((char*)fname)];
	int result = RLC_OK, key_len = AES_BYTE_LEN;
	uint8_t key[2*AES_BYTE_LEN], iv[AES_BYTE_LEN] = { 0 }, h[RLC_MD_LEN];
	FILE *inFile,*outFile;
	char *buffer,*buffer_o;
	int filelen,filelen_o;

	RLC_TRY {
		md_kdf(key, 2*key_len, pwd, strlen((char*)pwd));

		inFile = fopen(fname, "r");          // Open the file
		if(inFile == NULL) {
			printf("Error cannot find the file specified\n");
			return RLC_ERR;
		}
		fseek(inFile, 0, SEEK_END);          // Jump to the end of the file
		filelen = ftell(inFile);             // Get the current byte offset in the file
		rewind(inFile);                      // Jump back to the beginning of the file

		buffer = (char *)malloc(filelen * sizeof(char)); // Enough memory for the file
		fread(buffer, filelen, 1, inFile); // Read in the entire file
		fclose(inFile);

		filelen_o = AES_BYTE_LEN*(filelen/AES_BYTE_LEN);
		if(filelen % AES_BYTE_LEN!=0) {
			filelen_o+=AES_BYTE_LEN;
		}


		md_hmac(h, (uint8_t*)buffer, filelen - RLC_MD_LEN, key + key_len, key_len);
		if (util_cmp_const(h, buffer + filelen - RLC_MD_LEN, RLC_MD_LEN)) {
			result = RLC_ERR;
			free(buffer);
			return result;
		} else {
			buffer_o = (char *)malloc(filelen_o * sizeof(char));
			if (bc_aes_cbc_dec((uint8_t *)buffer_o, &filelen_o, (uint8_t *)buffer, filelen-RLC_MD_LEN, key, key_len, iv) != RLC_OK) {
				result = RLC_ERR;
			}
		}

		char* pos_ptr;
		strncpy(fname_o_temp,fname,strlen(fname)-4);
		fname_o_temp[strlen(fname)-4]='\0';
		pos_ptr = strrchr((char*)fname_o_temp, '.');
		strcpy(fname_o_ext,pos_ptr);
		strncpy(fname_o,fname_o_temp,strlen(fname_o_temp)-strlen(fname_o_ext));
		fname_o[strlen(fname_o_temp)-strlen(fname_o_ext)]='\0';
		if(option == F_KEEP) {
			//strcat(fname_o,"_dec");
		}
		strcat(fname_o,fname_o_ext);

		outFile = fopen(fname_o, "w");
		fwrite(buffer_o,filelen_o,1,outFile);
		fclose(outFile);

		free(buffer);
		free(buffer_o);
	}
	RLC_CATCH_ANY {
		result = RLC_ERR;
	}

	if (option == F_REMOVE) {
		remove(fname);
	}

	return result;
}


int abe_file_enc(char *fname, uint8_t *user_input_plc, mpk_t MPK, int option) {
	FILE *fp;
	int filelen;

	fp = fopen(fname, "r");          // Open the file
	if(fp == NULL) {
		printf("Error cannot find the file specified\n");
		return RLC_ERR;
	}
	fseek(fp, 0, SEEK_END);          // Jump to the end of the file
	filelen = ftell(fp);             // Get the current byte offset in the file
	rewind(fp);                      // Jump back to the beginning of the file

	uint8_t *msg = malloc(filelen * sizeof(char)); // Enough memory for the file
	fread((char*)msg, filelen, 1, fp); // Read in the entire file
	fclose(fp);

	plc_info_t PLC_INFO;
	plc_string_info_init(&PLC_INFO, user_input_plc);
	plc_string_info(&PLC_INFO, user_input_plc);

	uint8_t *plcnum = malloc(PLC_INFO.plc_num_str_size);
	uint8_t *plc = malloc(PLC_INFO.n_num_max_att * (2*ATT_HASH_LEN) + (PLC_INFO.n_num_max_att-1)*(strlen(ABE_PLC_AND)+2));

	plc_all_2_plcnum(plcnum, user_input_plc, PLC_INFO);

	plc_string_info_init(&PLC_INFO, plcnum);
	plc_string_info(&PLC_INFO, plcnum);

	plc_hash(plc,plcnum,PLC_INFO);

	abe_ct_t CT;
	abe_ct_set(&CT, MPK, plc, msg, filelen, PLC_INFO);

	char fname_o[22];
	sprintf(fname_o, "%s.enc", fname);
	abe_ct_exp(fname_o,&CT);

	if (option == F_REMOVE) {
		remove(fname);
	}

	abe_ct_free(&CT);
	free(msg);

	return 0;
}

/* ---------------------------------------Other hlib Operations--------------------------------------- */
int bin2hex(uint8_t* out , uint8_t* in, int in_len) {
	uint8_t hex_temp[3];
	for (int i = 0; i < in_len; i++)
	{
	    sprintf((char*)hex_temp,"%02X", in[i]);
	    strcat((char*)out,(char*)hex_temp);
	}
	out[2*in_len]='\0';
	return 0;
}

int check_user_regis(int* result, uint8_t* username, uint8_t* user_pass) {
	FILE *fp;
	fp = fopen(ABE_REGIS_FNAME,"r");
	if(fp == NULL) {
		printf("Error cannot find the file specified\n");
		*result = 1; // Error cannot find the file
		return RLC_ERR;
	}

	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	char *pos_ptr;
	char username_cmp[100];
	char user_pass_cmp[2*KDF_LEN+1];
	int found_username = 0;

	while ((read = getline(&line, &len, fp)) != -1) {
		pos_ptr = strstr(line, ",pass=");
		if(pos_ptr != NULL) {
			strncpy(username_cmp,line,pos_ptr-line);
			username_cmp[pos_ptr-line]='\0';
			if (strcmp(username_cmp,(char*)username)==0) {
				found_username = 1;
				strcpy(user_pass_cmp,pos_ptr+6);
				user_pass_cmp[2*KDF_LEN]='\0';
				break;
			}
		}
	}
	fclose(fp);

	if(found_username != 1) {
		printf("User has not registered\n");
		*result = 2; // User not registered
		return RLC_ERR;
	}

	uint8_t kdf_pwd[KDF_LEN];
	md_kdf(kdf_pwd, KDF_LEN, user_pass, strlen((char*)user_pass));

	uint8_t kdf_pwd_hex[KDF_LEN*2+1] = { '0' };
	bin2hex(kdf_pwd_hex , kdf_pwd, KDF_LEN);

	if (strcmp(user_pass_cmp,(char*)kdf_pwd_hex) != 0) {
		printf("User has input wrong password\n");
		*result = 3; // Wrong password
		return RLC_ERR;
	}

	*result = 0; // Found user in registration file and input correct password
	return 0;
}


int get_user_att_data(int* result, char* attdata, int *user_n_att, uint8_t* username) {
	FILE *fp;
	fp = fopen(ABE_ATTDATA_FNAME,"r");
	if(fp == NULL) {
		printf("Error opening attdata file\n");
		*result = 1; // Error cannot find the file
		return RLC_ERR;
	}

	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	char *pos_ptr, *pos_ptr2;
	char username_cmp[100];
	int found_username = 0;

	char user_str_n_att[10];

	while ((read = getline(&line, &len, fp)) != -1) {
		pos_ptr = strstr(line, ",n_att=");
		pos_ptr2 = strstr(line, ",att=[");
		if(pos_ptr!=NULL && pos_ptr2!=NULL) {
			strncpy(username_cmp,line,pos_ptr-line);
			username_cmp[pos_ptr-line]='\0';

			if (strcmp(username_cmp,(char*)username)==0) {
				found_username = 1;

				strncpy(user_str_n_att,pos_ptr+7,pos_ptr2-pos_ptr-7);
				user_str_n_att[pos_ptr2-pos_ptr-7] = '\0';
				*user_n_att = strtol(user_str_n_att, (char **)NULL, 10);

				strcpy((char*)attdata,pos_ptr2+5);
				break;
			}
		}
	}
	fclose(fp);
	//remove(ABE_ATTDATA_FNAME);

	if(found_username != 1) {
		printf("User is not in attribute database\n");
		*result = 2; // User is not in attribute database
		return RLC_ERR;
	}

	*result = 0; // User is in attribute database
	return 0;
}

int user_att_data_to_array(uint8_t** user_att, int user_n_att, char* attdata) {
	char *pos_ptr,*pos_ptr2;
	pos_ptr = strchr(attdata,'[');
	pos_ptr = pos_ptr + 1;
	for(int i=0; i<user_n_att; i++) {
		if(i==user_n_att-1) {
			pos_ptr2 = strchr(pos_ptr,']');
		} else {
			pos_ptr2 = strchr(pos_ptr,',');
		}
		strncpy((char*)user_att[i],pos_ptr,pos_ptr2-pos_ptr);
		user_att[i][pos_ptr2-pos_ptr]='\0';
		pos_ptr = pos_ptr2+1;
	}

	return 0;
}

int user_att_assess_for_attnum(int *max_att_len, int *user_n_att, uint8_t** user_att) {
	uint8_t *pos_ptr;
	int att_len;
	int n_attnum = *user_n_att;

	for(int i=0; i<*user_n_att; i++) {
		pos_ptr = (uint8_t*)strchr((char*)user_att[i],':');
		if (pos_ptr == NULL) {
			att_len = strlen((char*)user_att[i]);
		} else {
			n_attnum += ATT_NUM_BIT - 1;
			att_len = pos_ptr - user_att[i] + ATT_NUM_BIT + 2;
		}

		if(att_len>(*max_att_len)) {
			*max_att_len = att_len;
		}
	}
	(*user_n_att) = n_attnum;

	return 0;
}
