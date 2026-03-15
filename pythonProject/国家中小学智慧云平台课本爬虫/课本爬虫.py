# import webbrowser as w

url = """
https://basic.smartedu.cn/tchMaterial/detail?contentType=assets_document&contentId=ea2d167f-30e3-4c4b-9376-aa1c7be5929c&catalogType=tchMaterial&subCatalog=tchMaterial
"""
key = url.split('&')[1]
md5 = key.split('=')[1]
pdf_left = 'https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/'
pdf_right = '.pkg/pdf.pdf'
pdf_url = pdf_left + md5 + pdf_right
print('获取链接:', pdf_url, sep='\n')
# w.open(pdf_url)
