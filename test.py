from datetime import datetime
from numpy import*
def Newinsert(t,i):
    with open("ficherjdid.txt", "a") as f:
            date_obj = datetime.now()
            day = date_obj.strftime("%A")
            x = {
                    "tot": float(input("donner le montant de mois: ")),
                    "day": day,
                    "mas": input("chnwa srafet ===> "),
                    "dat": str(date_obj),
                    "mnt": float(input("9adech ====> ")),
                    "des": input("tfatheelll ====> "),
                    "cos": f"{date_obj.day}-{date_obj.month}-{date_obj.year}"
                }
            t[i]["tot"]=x["tot"]
            t[i]["day"]=x["day"]
            t[i]["mas"]=x["mas"]
            t[i]["mnt"]=x["mnt"]
            t[i]["des"]=x["des"]
            t[i]["dat"]=x["dat"]
            t[i]["cos"]=x["cos"]
            i=i+1
            last_day = t[i-1]["day"]# Get the last saved day if exists
            if last_day != day:
                x['day']="*"
                f.write("\n".join([f"{x['day']}:\nchnwa chrit=> {x['mas']}\n9adech srafet=> {x['mnt']}DT\nkifech=> {x['des']}\ndate=> {x['dat']}\n{x['cos']}", ""]))
                print("saved")
            else:
                f.write("\n".join([f"{x['day']}:\nchnwa chrit=> {x['mas']}\n9adech srafet=> {x['mnt']}DT\nkifech=> {x['des']}\ndate=> {x['dat']}\n{x['cos']}", ""]))
                print("saved")
    f.close()
    if input("t3awed t3abi (true/false): ").lower() != "false":
            Newinsert(t,i)
dict={
                    "tot":float(),
                    "day":str ,
                    "mas":str ,
                    "mnt":float(), 
                    "des":str,
                    "dat":str,
                    "cos":str,
                }          
t=array([dict]*10)
Newinsert(t,0)