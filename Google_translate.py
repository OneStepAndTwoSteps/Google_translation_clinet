import execjs
import requests
class Py4Js():

    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };

    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self ,text):
        return self.ctx.call("TL" ,text)

class translation():

    def __init__(self):
        self.URL="https://translate.google.cn/translate_a/" \
            "single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie" \
            "=UTF-8&oe=UTF-8&otf=1&ssel=0&tsel=0&kc=1&" \
            "tk={tk}&q={q}"
         self.URL2="https://translate.google.cn/translate_a/" \
                  "single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie" \
                  "=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&" \
                  "tk={tk}&q={q}"
        self.HEADERS={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def work(self):
        while True:
            content=input("请输入你要翻译的内容：")
            if content == "q!":
                break
            Js = Py4Js()
            tk = Js.getTk(content)
            q = content
            
            if content.isalpha():
                response = requests.get(self.URL2.format(tk=tk, q=q), headers=self.HEADERS).json()
                print("response", response)
                word = response[0][0][0]
                Chinese_character = response[0][0][1]
                print("\n翻译结果：%s %s \n" % (Chinese_character,word))
            else:
                response = requests.get(self.URL.format(tk=tk, q=q), headers=self.HEADERS).json()
                print("response",response)
                word=response[0][0][0]
                Chinese_character=response[0][0][1]
                # word2 = response[1][0][0]
                # Chinese_character2 = response[1][0][1]
                print("\n翻译结果：%s %s \n"%(word,Chinese_character))
if __name__ == '__main__':
    try:

        run=translation()
        run.work()
    except:
        print("程序报错")
