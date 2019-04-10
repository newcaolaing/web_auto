from mock import mock
#模拟mock 封装
def mock_test(url,request_data,method,response_data,mock_method=False):
	mock_method = mock.Mock(return_value=response_data)
	res = mock_method(url,method,request_data)
	return res


res = mock_test("http://127.0.0.1",{'1':1},"get",{2:2}	)
print(res)