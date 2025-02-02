from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum 

app = FastAPI()

# In-memory data (replace with a database or other storage in a real app)
marks_data = {
                "ulKIIc":41,
                "0Sg":54,
                "i2GvVpuIs":83,
                "nrQCnhBPky":4,
                "fhi":30,
                "lNwTIPsxX":26,
                "bGqreiQkZf":61,
                "qdZpO7Qe":70,
                "hHMYPC":0,
                "Ky2":94,
                "bFJnssa1Pc":4,
                "86Tk0um4q":24,
                "zW9gZcg":11,
                "14A":14,
                "fCvsRTpp":41,
                "3p2W":62,
                "B6a":86,
                "QOUfdT":71,
                "QcoCRMJv":16,
                "ZMQn9wLJRW":32,
                "GDm52":54,
                "iJMM1Crgh":30,
                "agaA":97,
                "v6":96,
                "r1cXBp8":37,
                "zg7obK":44,
                "KN":75,
                "hY":57,
                "z":43,
                "Crm":0,
                "S":98,
                "JV":33,
                "yzG":61,
                "B2DlaFHUN":69,
                "Om":42,
                "M1Dw":43,
                "1WS7Xf":53,
                "9LRkqK":5,
                "eFxv789":15,
                "N80df":32,
                "bTYl":22,
                "v1IngPygd":90,
                "Y11xXV":89,
                "QoA4":76,
                "no":62,
                "oh":9,
                "hTa":38,
                "AkfFXQBU3":69,
                "OeE8d2":5,
                "k0w3cnppl":53,
                "b":7,
                "ScD9jWn":92,
                "wQsTUY3Ej":42,
                "ONRuXySLT":75,
                "Ogr":63,
                "xXbFa4o27":16,
                "lw7V":69,
                "nb7ho":78,
                "Vm4":67,
                "Y7N8REXG":59,
                "AlXkLt":88,
                "ewdtyQv":20,
                "2SelWO":72,
                "hrBtPpSFG":22,
                "c1NxXF":40,
                "C":7,
                "QkePQ2EkeX":99,
                "Dk":83,
                "wZa":73,
                "h4j":26,
                "GH":42,
                "kIDGr":43,
                "4TuJz":59,
                "U9Ml7":1,
                "92kjHnAM":3,
                "ENOL":0,
                "T9nmZP8":5,
                "9Fe":39,
                "cE":53,
                "8WWjgrD9zj":23,
                "HaTpoZOsmw":52,
                "hsycJ":10,
                "kf2S88Z":61,
                "1a2e7":52,
                "o":62,
                "k7dgVMHa":69,
                "C6vmZZ":25,
                "DA58Ec":10,
                "znrVfWYOBo":54,
                "SUkjEeuq":43,
                "mI":2,
                "Mngz":95,
                "YaoPdZrllI":31,
                "3NRc":11,
                "5iq":57,
                "H":58,
                "n":79,
                "gkZhdQ":36,
                "Sdrvwt1":90,
                "FsjWe":77
            }
            



origins = ["*"]  # Allow all origins (for demonstration - restrict in production)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Home Page"

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):  # '...' makes it required
    results = {}
    result_list = []
    print(name)
    for n in name:
        print(n)
        print(marks_data[n])
        if n in marks_data:
            results[n] = marks_data[n]
            result_list.append(marks_data[n])
        else:
            results[n] = "Not Found"
    
    return {"marks" : result_list}



# # For local testing (optional)
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)  # Or any port you prefer

handler = Mangum(app)