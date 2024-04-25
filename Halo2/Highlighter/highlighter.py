#I DO NOT WARRANTY THIS CODE TO BE BUG FREE OR TO BE FIT FOR PURPOSE, RUNNING HIGHLIGHTER AGAINST A PROJECT DOES NOT GUARANTEE THAT THE PROJECT IS SECURE AND/OR BUG FREE
from subprocess import PIPE,Popen
import random
import os
import glob
import json

def runHighlight(project_dir,rules_dir):
    # Used for progress output
    print("---START--------------------------------------------------------------------\n")
    # Used for report output
    MarkdownString = "# HighLighter Report\n"
    print("[+] Running Highlighter against directory: ",project_dir)
    MarkdownString = MarkdownString + "- Running Highlighter against directory: " + project_dir + "\n"
    print("\n")
    print("[+] Rules templates directory set as : ",rules_dir)
    MarkdownString = MarkdownString + "- Rules templates directory set as : " + rules_dir + "\n"
    print("\n")
    try:
        # First import all templates to minimise IO
        # Rules are stored in the rules array
        rules = []
        rulecheckfinds = ""
        for jsonfile in os.listdir(rules_dir):
            with open(rules_dir + "/" + jsonfile, 'r', encoding="utf-8") as rulefile:
                ruleEntry = rulefile.read()
                rule = json.loads(ruleEntry)
                rules.append(rule)
                
        # Now check for files that implement the Circuit trait    
        circuitlist = "## Circuit files found:\n"
        # Walk all directories and subdirectories from the main folder which was set in project_dir
        for root,dirs, files in os.walk(project_dir):
            for file in files:
                # Only read files ending in ".rs"
                if file.endswith(".rs"):
                    with open(os.path.join(root,file), 'r', encoding="utf-8") as rustfile:
                        rustcode = rustfile.read()
                        # For now just check for text as below which should find "> Circuit<Fp> for "
                        if rustcode.find("> Circuit<") > 0:
                            circuitlist = circuitlist + "   [^] " + file + "\n"
                        # Now loop through the rules array and check the "match" value against the code 
                        # retrieved from reading the source file
                        for rule in rules:
                            intfound = 0
                            for strmatch in rule["match"]:
                                if rustcode.find(strmatch) > 0:
                                    # The counter makes sure it only lists the file once 
                                    # and not for each match in a file
                                    if intfound == 0:
                                        intfound = 1
                                        rulecheckfinds = rulecheckfinds + "### File: " + os.path.join(root,file) + "\n   #: Match found on : " + strmatch + "\n   #: " + rule["description"] + "\n\n"
                                        # setup the file path
                                        filepath = os.path.join(root,file)
                                        # Use Popen to open grep the "match" value in the file
                                        # and capture the output
                                        with Popen("grep -n -C 1 '" + strmatch + "' " + filepath + " -rIs",shell=True,stdout=PIPE) as proc:
                                            try:
                                                out, errs = proc.communicate(timeout=15)
                                            except TimeoutExpired:
                                                proc.kill()
                                                out, errs = proc.communicate()
                                            bashOutput = out.decode()
                                        # String to concatenate all match finds
                                        rulecheckfinds = rulecheckfinds + "```\n" + bashOutput + "\n```\n"
                        
                            
        print(circuitlist)
        print("## Rule checks returned the list of code to check below:\n") 
        rulecheckfinds = "## Rule checks returned the list of code to check below:\n" + rulecheckfinds
        print(rulecheckfinds)
        print("---END----------------------------------------------------------------------")
        # Setup final string to write out to report
        MarkdownString = MarkdownString + circuitlist + rulecheckfinds
        
        #Write out the markdown into the report file
        f = open("HighLighterReport.md", "w")
        f.write(MarkdownString)
        f.close()
    except Exception as e:
        print("[#### ] Highlighter ran into an exception : ",e)

def main():
    #Setup python argument parsing    
    import argparse
    parser = argparse.ArgumentParser()
    # 2 arguments used
    # project_dir ---> is the fully qualified path to the HALO2 project folder
    # rules_dir   ---> is the fully qualified path to the templates directory in 
    #                   most cases will be one level down for here
    parser.add_argument("project_dir", help="The project directory")
    parser.add_argument("rules_dir", help="The directory which has the JSON rules templates to check against")
    args = parser.parse_args()
    # Parse the arguments and call the runHighlight function
    runHighlight(args.project_dir, args.rules_dir)

main()
