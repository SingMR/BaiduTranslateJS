# coding=gbk
import execjs
import requests
import json
import sys
import io

class BaiDuFanYi():
    def __init__(self):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.chi_eng = 'https://fanyi.baidu.com/langdetect'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            'origin': 'https://fanyi.baidu.com',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'cookie': 'BAIDUID=82CB7EFD1337E15DDF738EE42DE7B0A8:FG=1; BIDUPSID=82CB7EFD1337E15DDF738EE42DE7B0A8; PSTM=1560480974; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=mIyR0dIcm9YdHdCN0pqalZFT05Qa0Z3Qi1VdzRCVlpBOW9MZFg2QWh5dXV-QVplSVFBQUFBJCQAAAAAAAAAAAEAAADb7UmOztLRp3B5dGhvbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK5v312ub99dc; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; APPGUIDE_8_2_2=1; H_PS_PSSID=; yjs_js_security_passport=cbd6cea40303f73e225caddf5f66503557b5ffea_1577334640_js; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1577295575,1577334629,1577334640,1577334851; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1577334851; __yjsv5_shitong=1.0_7_e2be0c5a3e37fbb73127470170c38caf2a74_300_1577334850593_121.13.42.131_6585855f'
        }
        self.word = input('输入要翻译的内容：(如果退出输入esc!!!)')


    def sign(self):
        with open('baidu.js', 'r', encoding='utf8') as f:
            ctx = execjs.compile(f.read())
        sign = ctx.call('e', self.word)
        return sign

    def get_chi_eng(self):
        data = {"query": self.word}
        response = requests.get(url=self.chi_eng,headers=self.headers,params=data)
        res = json.loads(response.content.decode(),encoding='utf8')
        content = res['lan']
        return content

    def sendpost(self):
        form_data = {
                'from': 'zh' if self.get_chi_eng() == 'zh' else 'en',
                "to": 'en' if self.language == '1' else 'zh',
                'query': self.word,
                "simple_means_flag": "3",
                "sign":self.sign(),
                "token": "07b78d19657eafd3358691e412a21801"
         }

        response = requests.get(url=self.url,headers=self.headers,params=form_data)
        response = json.loads(response.text)
        # print(response)
        res = response['trans_result']['data'][0]['dst']
        print('翻译的结果为: %s' %res)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') # 改变标准输出的默认编码
    while True:
        fanyi = BaiDuFanYi()
        if fanyi.word == 'esc':
            exit()
        fanyi.sendpost()

