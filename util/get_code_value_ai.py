from PIL import Image
# from setting.ShowapiRequest import ShowapiRequest
import time

# https://www.showapi.com/api/view/184/4

# class GetCode:
#     """获取验证码图片，解析验证码图片并返回验证码值"""
#     def __init__(self, driver):
#         self.driver = driver
#
#     def get_code_image(self, file_name):
#         self.driver.save_screenshot(file_name)
#         code_element = self.driver.find_element_by_id("getcode_num")
#         left = code_element.location['x']
#         top = code_element.location['y']
#         right = code_element.size['width'] + left
#         height = code_element.size['height'] + top
#         im = Image.open(file_name)
#         img = im.crop((left, top, right, height))
#         img.save(file_name)
#         time.sleep(1)
#
#     # 解析图片获取验证码
#     def code_online(self, file_name):
#         self.get_code_image(file_name)
#         r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
#         r.addBodyPara("typeId", "35")
#         r.addBodyPara("convert_to_jpg", "0")
#         r.addFilePara("image", file_name)  # 文件上传时设置
#         res = r.post()
#         # print("test_demo:",res.text)
#         time.sleep(1)
#         text = res.json()['showapi_res_body']
#         # print(text)
#         try:
#             code = text['Result']
#             return code
#         except Exception as e:
#             print('code_error:',e)
#             return None