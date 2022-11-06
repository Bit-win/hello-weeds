# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 08:25:10 2022

@author: Master Zhang
"""

import requests
from bs4 import BeautifulSoup
url = 'https://member1.taobao.com/member/fresh/deliver_address.htm?spm=0.0.0.0.OLY6Xh'



headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    'cookie':'_m_h5_tk=af6caf031cfacf2f2436d05b891dc38c_1661652994010; _m_h5_tk_enc=ba09a1cad033cc977decdbfb1608ba99; cna=KXNRGwc9AGACAbfA5cws5cQW; t=3e5cb41fe65d1a2d1f95ffd4ddc905ed; _tb_token_=e3870943f53e3; xlly_s=1; cookie2=1e2dfcc7412e309e9d04b2995031d4c3; thw=cn; _samesite_flag_=true; sgcookie=E100%2BWkLUsuZYT3iQy3mmYY34L2e8LaEXTkRK7muIAAfq40f7mEh9l8UMKBWC3DzTBDFCfMulonUQztnytX9v8N8zLeWn5e4%2FVXjJGqaMrTt9%2Bp0x2KnSwjtqsi8KtAIOE2B; unb=2538375199; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UU2xrR5Y3IpmXQ%3D%3D&vt3=F8dCv4fZpy57MCJ4BW8%3D&nk2=0%2FI0z2wM6OxjaoKwNM2O4Q%3D%3D; csg=0e439637; lgc=%5Cu5B89%5Cu5B9A%5Cu81EA%5Cu7136%5Cu968F%5Cu9047%5Cu800C%5Cu5B89; cancelledSubSites=empty; cookie17=UU2xrR5Y3IpmXQ%3D%3D; dnk=%5Cu5B89%5Cu5B9A%5Cu81EA%5Cu7136%5Cu968F%5Cu9047%5Cu800C%5Cu5B89; skt=71d1d340bda8bfc4; existShop=MTY2MTY0NTk3Mw%3D%3D; uc4=id4=0%40U2%2F2uUSIBi4U76fDYN%2BBTd1R5kB%2B&nk4=0%400UmEiyHgtZTfkAathC%2BVoMAY5E4WwGLHrU7p; tracknick=%5Cu5B89%5Cu5B9A%5Cu81EA%5Cu7136%5Cu968F%5Cu9047%5Cu800C%5Cu5B89; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%AE%899b; _nk_=%5Cu5B89%5Cu5B9A%5Cu81EA%5Cu7136%5Cu968F%5Cu9047%5Cu800C%5Cu5B89; cookie1=VFR74YWxO38XZh7ysoJeF%2FwNQyi7Qa8LbS0TS2eH5Kw%3D; mt=ci=58_1; v=0; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cart_m=0&cookie14=UoeyD4Sgxkn%2FJw%3D%3D&pas=0&existShop=false&cookie21=V32FPkk%2FgihF%2FS5nr3O5; tfstk=cwmABJtMnQAm_vzQ5xLu7rC1Sy9lZ2XYstNOXcR5oi-DAksOi-mnv6HMlRPUMLC..; isg=BJycKnDoE6XL-OU0GKz-SFrYbbpOFUA_qDYnJXafawdWwT5LniU_zl9zISk5yXiX; l=eBLkmAa4gUtXPgFoBO5CFurza779qQRbzsPzaNbMiInca18A9UQvNNCE_ZvpWdtjgtfFSetrEOC81dpxk3UpgujUxKtWPQ3HeYJw-',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    
    }





r = requests.get(url,headers = headers)

soup = BeautifulSoup(r.text,"html.parser")

soup.find_all('span',class_ ="next-table-cell-wrapper" )
