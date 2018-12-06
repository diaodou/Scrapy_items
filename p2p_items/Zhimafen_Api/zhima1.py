










start_url = 'http://api.qhweidai.com/api/topicture'
def start_requests(self):
    for i in self.open_file():
        s = i.strip()
        #s = 'http://upload.51qianmai.com/20180126064925821.jpg'
        data = {'channel':'abc','picturl':s}
    #data = {'channel':'abc','picturl':i}
        #yield FormRequest(url=self.start_url,formdata=data,callback=self.parse,meta={'url':s})



def save_file(url):
    with open('C:\\Users\\99329\\Desktop\\error17.txt', 'a') as f:
        f.write(url + '\n')
        print('成功写入！')
def open_file(self):
    with open('C:\\Users\\99329\\Desktop\\5.txt', 'r') as f:
        origin = f.readlines()
        return origin

def open_files(self):
    with open('C:\\Users\\99329\\Desktop\\parse_json.txt', 'r') as f:
        origin = f.readlines()
        return origin
