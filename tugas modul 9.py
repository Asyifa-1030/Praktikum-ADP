import os
import time
from termcolor import colored
os.system('cls')
   
def aplikasi():
    print(colored("""      
RRRR    AAAAA  N   N  Y   Y
R   R   A   A  NN  N   Y Y 
RRRR    AAAAA  N N N    Y  
R  R    A   A  N  NN    Y  
R   R   A   A  N   N    Y  
""", 'cyan', attrs=['bold']))
    print(colored("Selamat datang di aplikasi RANY!", 'magenta'))

def loading(proses):
    jumlah_tanda = proses // 10
    bagian_terisi = "" * jumlah_tanda       
    bagian_kosong = "." * (10 - jumlah_tanda)
    baris=f"{bagian_terisi}{bagian_kosong}{proses}%"
    return baris

def loading2():
    print(colored("Memuat aplikasi...", 'yellow'))
    for proses in range(0, 101, 10):
        baris= loading(proses)
        print(colored(baris, 'green'), end='\n')
        time.sleep(0.5)
    print("\n")
    print(colored("Aplikasi RANY berhasil dimuat!", 'green'))

aplikasi()
loading2()