#include <main.h>	



int main() {
	if (init_param_set() != RLC_OK) {
		core_clean();
		return 1;
	}
	
	h1_decryption();
	
	return 0;
}
