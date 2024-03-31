import sys
import os
 
path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
complete_path = os.path.join(path1, "Microbots")
sys.path.append(complete_path)
 
from license_check import check_license
from final_excution import main_excution
 
 
def main():
    try:
        if check_license():
            main_excution()
           
 
    except Exception as e:
        error_message = str(e)
        print(f"{error_message}")
 
if __name__ == "__main__":
    main()
