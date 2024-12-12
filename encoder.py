import re
import datetime
import math
import time
import random
import json
import requests
import os
from javascript import require

class Encoder:
    def __init__(self, version):
        if os.path.exists("./map.json"):
            with open('./map.json', 'r') as f:
                self.mapp = json.load(f)
        else:
            self.mapp = {}
            
        if version not in self.mapp:
            self.mapping, self.mapping_num = self.fetcher(version)
        else:  
            self.mapping = self.mapp[version]['mapping']
            self.mapping_num = int(self.mapp[version]['mapping_num'])
            
        self.zA = 83
        self.OA = datetime.datetime.now().hour
        self.YA = -3203492822000
        timestamp = float(time.time() * 1000)
        self.NA = float(f"{str(timestamp).replace('.', '')[:13]}.{str(timestamp)[14]}")
        self.fA = math.floor(254 * random.random())
        
        self.SA = int((self.YA + self.OA + self.NA) * self.fA)
        self.cA = int(self.SA + self.mapping_num)

        if self.cA < 0:
            self.cA = 1 + ~self.cA
        else:
            self.cA = self.cA
            
        self.LA = 1 + int(((1664525 * (self.cA + 1013904223)) % 4294967296) / 4294967296 * 82)
        
        oA = self.ooA(self.SA, self.LA)
        self.nA = oA[0]
        self.rA = oA[1]
        self.xA = re.compile(r'[a-z\d.,/#!$%^&*;:{}=\-_~()\s]', re.IGNORECASE)
        
    def fetcher(self, version):
        self.jsdom = require('jsdom')
        self.evaluate = require("vm").Script
        self.vm = self.jsdom.JSDOM("<title></title>", {"runScripts": "dangerously"}).getInternalVMContext()
        hsw = requests.get(f'https://newassets.hcaptcha.com/c/{version}/hsw.js').text
        num = int(hsw.split("=~~(A+")[1].split("),")[0])
        if '".split("")' in hsw:
            mapping = hsw.split('".split("")')[0].split('="')[1]
        elif ')](""),' in hsw:
            obf_char = hsw.split('={},')[1].split("=")[1].split("(")[0]
            param = hsw.split("={},")[1].split(f"={obf_char}(")[1].split(")")[0]
            index = hsw.split(f",{param}=")[1].split(",")[0]
            mapping = self.decode(index, hsw)
            
        if version not in self.mapp:
            self.mapp[version] = {}
            
        self.mapp[version]['mapping'] = mapping
        self.mapp[version]['mapping_num'] = num
        
        with open('./map.json', 'w') as f:
            json.dump(self.mapp, f, indent=4)
        
        return mapping, num
 
    def decode(self, index, hsw):
        func = hsw.split("(){return!0}))}function ")[1].split("(")[0]
        hsw = hsw.replace("if(0===A)", f"if(2===A)return {func}({index});if(0===A)")
        self.evaluate(hsw).runInContext(self.vm)
        result = self.evaluate(f"hsw(2)").runInContext(self.vm)
        return result
 
    def ooA(self, A, Q):
        C = int(A + self.mapping_num)  
        g = C if C >= 0 else 1 + ~C 
        
        D = {}
        M = list(self.mapping)
        
        w = self.zA 
        while w:
            g = (1103515245 * g + 12345) & 2147483647
            E = g % w
            I = M[w - 1]
            M[w - 1] = M[E]
            M[E] = I
            D[M[w - 1]] = (w + Q) % self.zA
            w -= 1
        
        D[M[0]] = (0 + Q) % self.zA
        
        return D, ''.join(M)

    def encode(self, A):
        I = str(A)
        C = self.rA
        D = len(I)
        temp = I + C[D:self.zA]
        temp = ' '.join(temp.split()[::-1])
        temp = temp[::-1]
        
        def mmap(A):
            if self.xA.match(A):
                C = self.nA[A]
                return self.rA[(C + self.LA) % self.zA]
            return A
        
        return ''.join(map(mmap, temp))

encoder = Encoder('cc9cbcc44893d9601186ed793b76ac72a56a3e176be51252819b38f7d2f1f97c')

res = encoder.encode('ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x00009A49) Direct3D11 vs_5_0 ps_5_0, D3D11)')
print(res) 
# output -> K*TH6.y=U XQq.:2q=U XQ.:2qIs8Q.Up.ICsJ#/8T.:%n6%PPPPtPq.^^}) CU8s}.PwBwIo.yPwBwI#.:^^})} 
# THE OUTPUT WILL BE DIFFERENT EVERY TIME DUE TO USE OF RANDOM NUMBERS & TIMESTAMPS
