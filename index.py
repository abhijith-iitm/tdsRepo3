# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message":"Hello World!"}


# api/main.py (FastAPI app)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# In-memory data (replace with a database or other storage in a real app)
marks_data = {
                {"name":"ulKIIc","marks":41},
                {"name":"0Sg","marks":54},
                {"name":"i2GvVpuIs","marks":83},
                {"name":"nrQCnhBPky","marks":4},
                {"name":"fhi","marks":30},
                {"name":"lNwTIPsxX","marks":26},
                {"name":"bGqreiQkZf","marks":61},
                {"name":"qdZpO7Qe","marks":70},
                {"name":"hHMYPC","marks":0},
                {"name":"Ky2","marks":94},
                {"name":"bFJnssa1Pc","marks":4},
                {"name":"86Tk0um4q","marks":24},
                {"name":"zW9gZcg","marks":11},
                {"name":"14A","marks":14},
                {"name":"fCvsRTpp","marks":41},
                {"name":"3p2W","marks":62},
                {"name":"B6a","marks":86},
                {"name":"QOUfdT","marks":71},
                {"name":"QcoCRMJv","marks":16},
                {"name":"ZMQn9wLJRW","marks":32},
                {"name":"GDm52","marks":54},
                {"name":"iJMM1Crgh","marks":30},
                {"name":"agaA","marks":97},
                {"name":"v6","marks":96},
                {"name":"r1cXBp8","marks":37},
                {"name":"zg7obK","marks":44},
                {"name":"KN","marks":75},
                {"name":"hY","marks":57},
                {"name":"z","marks":43},
                {"name":"Crm","marks":0},
                {"name":"S","marks":98},
                {"name":"JV","marks":33},
                {"name":"yzG","marks":61},
                {"name":"B2DlaFHUN","marks":69},
                {"name":"Om","marks":42},
                {"name":"M1Dw","marks":43},
                {"name":"1WS7Xf","marks":53},
                {"name":"9LRkqK","marks":5},
                {"name":"eFxv789","marks":15},
                {"name":"N80df","marks":32},
                {"name":"bTYl","marks":22},
                {"name":"v1IngPygd","marks":90},
                {"name":"Y11xXV","marks":89},
                {"name":"QoA4","marks":76},
                {"name":"no","marks":62},
                {"name":"oh","marks":9},
                {"name":"hTa","marks":38},
                {"name":"AkfFXQBU3","marks":69},
                {"name":"OeE8d2","marks":5},
                {"name":"k0w3cnppl","marks":53},
                {"name":"b","marks":7},
                {"name":"ScD9jWn","marks":92},
                {"name":"wQsTUY3Ej","marks":42},
                {"name":"ONRuXySLT","marks":75},
                {"name":"Ogr","marks":63},
                {"name":"xXbFa4o27","marks":16},
                {"name":"lw7V","marks":69},
                {"name":"nb7ho","marks":78},
                {"name":"Vm4","marks":67},
                {"name":"Y7N8REXG","marks":59},
                {"name":"AlXkLt","marks":88},
                {"name":"ewdtyQv","marks":20},
                {"name":"2SelWO","marks":72},
                {"name":"hrBtPpSFG","marks":22},
                {"name":"c1NxXF","marks":40},
                {"name":"C","marks":7},
                {"name":"QkePQ2EkeX","marks":99},
                {"name":"Dk","marks":83},
                {"name":"wZa","marks":73},
                {"name":"h4j","marks":26},
                {"name":"GH","marks":42},
                {"name":"kIDGr","marks":43},
                {"name":"4TuJz","marks":59},
                {"name":"U9Ml7","marks":1},
                {"name":"92kjHnAM","marks":3},
                {"name":"ENOL","marks":0},
                {"name":"T9nmZP8","marks":5},
                {"name":"9Fe","marks":39},
                {"name":"cE","marks":53},
                {"name":"8WWjgrD9zj","marks":23},
                {"name":"HaTpoZOsmw","marks":52},
                {"name":"hsycJ","marks":10},
                {"name":"kf2S88Z","marks":61},
                {"name":"1a2e7","marks":52},
                {"name":"o","marks":62},
                {"name":"k7dgVMHa","marks":69},
                {"name":"C6vmZZ","marks":25},
                {"name":"DA58Ec","marks":10},
                {"name":"znrVfWYOBo","marks":54},
                {"name":"SUkjEeuq","marks":43},
                {"name":"mI","marks":2},
                {"name":"Mngz","marks":95},
                {"name":"YaoPdZrllI","marks":31},
                {"name":"3NRc","marks":11},
                {"name":"5iq","marks":57},
                {"name":"H","marks":58},
                {"name":"n","marks":79},
                {"name":"gkZhdQ","marks":36},
                {"name":"Sdrvwt1","marks":90},
                {"name":"FsjWe","marks":77}
            }



origins = ["*"]  # Allow all origins (for demonstration - restrict in production)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)


@app.get("/api?name=X&name=Y")
async def get_marks(name: str = None):
    names = []
    if name:
        names.append(name)
    # Handle multiple names (e.g., /api?name=X&name=Y)
    # FastAPI automatically handles query parameters in this way
    # Note: If you have names as list, use Query parameter like this:
    # from typing import List
    # @app.get("/api")
    # async def get_marks(name: List[str] = Query(None)):
    #     names = name
    else:
        raise HTTPException(status_code=400, detail="At least one name must be provided")

    marks = []
    for n in names:
        mark = marks_data.get(n)
        if mark is not None:
            marks.append(mark)
        else:
            raise HTTPException(status_code=404, detail=f"Name '{n}'
                             not found")

    return {"marks": marks}



# For local testing (optional)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # Or any port you prefer