src = "out/result_llama-2-7b-chat_multiarith_decomp_llama-2-7b-chat_mathreg.json"

import json

num_correct = 0
num_tot = 0
with open(src, "r") as f:
    res = json.load(f)
    for item in res:
        gt = item["final_ans"]
        out = item["answer"]
    
        if "gsm8k" in src:
            gt = gt.split("#### ")[-1]
        try:
            if abs(float(gt) - float(out)) <= 1e-5:
                num_correct += 1
        except:
            num_correct += 0
        
        num_tot += 1

print(num_correct / num_tot)
