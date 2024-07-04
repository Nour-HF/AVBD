import os
import time
import subprocess


def runCommands():

    #process = subprocess.Popen(['python3', 'translator.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    #process.communicate(input='ExampleInvoiceBT')

    #time.sleep(2)

    #Create mapping using Yarrrml parser using the defined yml file
    os.system("yarrrml-parser -i testMapping.yarrrml -o RML.rml.ttl")

    #wait until the .ttl is generated
    time.sleep(1)

    #Generate the knowledge graph using RMLMapper
    os.system("java -jar rmlmapper.jar -m RML.rml.ttl -o knowledgeGraph.ttl")

    #wait until the knowledge graph is generated
    #time.sleep(3)