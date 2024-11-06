#include <main.h>



int main() {
	if (init_param_set() != RLC_OK) {
		core_clean();
		return 1;
	}

	h2_user_regis();

	return 0;
}
