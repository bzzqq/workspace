raw = '偄偮偐丄偒傒偵夛偆擔傑偱'
raw_encode = raw.encode('gbk')
raw_encode.decode('shift-jis')

a = '''偁偺偹偣偐偄偼偠偮偼偮側偑偭偰偄傞傫偩偭偰
偩偐傜偨偲偊偼側傟偰偟傑偭偰傕傒傫側傂偲傝偠傖側偄
偨偄偣偮側傂偲偲偼偄偮傑偱傕偢偭偲偳偙偐偱偮側偑偭偰偄傞偺偝'''
a.encode('gbk').decode('shift-jis')
print(a.encode('gbk').decode('shift-jis'))
