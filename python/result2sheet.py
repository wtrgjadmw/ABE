import os, pandas

all_results_df = pandas.DataFrame()

result_dir = "../multiRAM_multiMAS_16mux/scheduling_result"
configs = sorted(os.listdir(result_dir))

for config in configs:
    results_df = pandas.Series(index=["MUL", "EP2_ADD_w_EVAL", "EP2_DBL_w_EVAL", "SPARSE", "SQR", "SQR012345", "EP_ADD_A_0", "EP_ADD_A_ANY", "EP_DBL_A_0", "EP_DBL_A_ANY", "ISOGENY", "FP12_INV_BEFORE_FPINV", "FP12_INV_AFTER_FPINV", "2xSSWU_BEFORE_EXP", "2xSSWU_AFTER_EXP", "EP_YRECOVER", "EP2_LADDERMUL", "EP2_YRECOVER", "FP12_LADDERMUL"], name=config)
    for operation in os.listdir("{}/{}".format(result_dir, config)):
        solution = []
        exec(open("{}/{}/{}/result.txt".format(result_dir, config, operation), 'r', encoding="utf-8").read(), globals())
        results_df.loc[operation] = int(solution[-1][-1])
    all_results_df = pandas.concat([all_results_df, results_df], axis=1)
    print(all_results_df)




# for root, dirs, files in os.walk("../../multiRAM_multiMAS_16mux/scheduling_result/"):
#     print(dirs)