import sys,json
from culinara.culinara_manager import CuinaraManager



def main():
    args = sys.argv
    # args =  ["main.py","plan"]
    if len(args) < 2:
        print("Please provide necessary commands to run the program.")
        return

    if args[1].lower() != 'plan' and args[1].lower() != 'manage':
        print("Invalid commands.")
        return 
    
    with open(".\\config.json","r") as f:
        paths = json.load(f)
    cm = CuinaraManager(paths)
    if args[1].lower() == 'plan':
        cm.plan_mod(args)
        return
    else:
        cm.manage_mod()
        return


main()

