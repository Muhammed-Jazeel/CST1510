"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

#raw_records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

#for raw_record in raw_records:
   # pass   # replace with your code


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring


# =================================================================== FUNCTIONS
# 1. parse_line cleans one messy line; status_of decides the status.

def parse_line(raw_line):
    """turn one messy line into a clean dict."""
    line = raw_line.strip() #removes spaces from both the end
    hostname_part, rest = line.split(",", 1) #cuts at the first comma only (1)
    hostname = hostname_part.strip().lower() #converts it to lowercase

    record = {"hostname": hostname} #start the dict with hostname
    for piece in rest.split(","): #split the rest into key value pieces
        key, value = piece.split("=") #cuts each piece "=" into key and value
        record[key.strip().lower()] = float(value.strip()) #clean the key turn the value into a number, store it

    return record 


def status_of(used, total):
    """returns overlimit, status, or warning """
    percent = used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


raw_records = [] #empty lists collect the lines from the file
with open("messy_lines.txt") as f:
    for line in f: #go through the file one line at a time
        if line.strip() != "":          #skip blank lines
            raw_records.append(line) # adds it to the empty list

flagged_count = 0 #counter to flag the hosts
for raw_record in raw_records: # go through each messy line, clean it into a dict, get its status, and show the dict and its status
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])
    print(record, "=", status)

    if status != "OK": #warning or over limit flagged +1 adds to the counter
        flagged_count += 1

print(f"\n{len(raw_records)} records checked, {flagged_count} flagged") #one line summary at the end