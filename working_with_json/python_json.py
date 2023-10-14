import json,os

params_file="option.json"


if os.path.exists( params_file ):
    try:
        with open( params_file, 'r' ) as params:
            data = json.load(params)
            if "greenLight" in data and data["greenLight"] == True:
                print(data["greenLight"])
                print("Turn on")
            else:
                print("No Green light option found")
    except Exception as e:
        print("Error" + str(e))
        exit(3)