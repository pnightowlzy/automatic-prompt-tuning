import concurrent.futures
import utils
from tqdm import tqdm
def print_out(a):
    return a+1, a+2, a+3

def multi_process():
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(print_out, i) for i in range(100)]
        for i, future in tqdm(enumerate(concurrent.futures.as_completed(futures)), total=len(futures), desc="running print stage"):
            print("start to process")
            a,b,c = future.result()
            print(a, b, c)

if __name__ == '__main__':    
    response = utils.chatgpt(
        "你好",
        max_tokens=512,
        n=1,
        timeout=10,
        temperature=0        
    )
    print(response)