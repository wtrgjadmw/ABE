#include <main.h>

/* ---------------------------------------Main--------------------------------------- */
int main() {
	if (init_param_set() != RLC_OK) {
		core_clean();
		return 1;
	}

	//h1_system_setup();
	//h1_edit_att();
	//h1_user_regis();
	//h1_encryption();
	//h1_decryption();

	//h2_system_setup();
	//h2_user_regis();
	//h2_encryption();
	h2_decryption();

	return 0;
}
