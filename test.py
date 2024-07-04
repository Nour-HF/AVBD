import os
import time
import subprocess
import translator


process = subprocess.Popen(['python3', 'translator.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout = process.communicate(input='ExampleInvoiceBT')

#print(stdout)

