#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

def lists(selection):

    pinYin = [ 'ba', 'bai', 'ban', 'bang', 'bao', 'bei', 'ben', 'beng', 'bi', 'bian', 'biao', 'bie', 'bin', 'bing', 'bo', 'bu', 'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cen', 'ceng', 'cha', 'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chi', 'chong', 'chou', 'chu', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo', 'ci', 'cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo', 'da', 'dai', 'dan', 'dang', 'dao', 'de', 'deng', 'di', 'dian', 'diao', 'die', 'ding', 'diu', 'dong', 'dou', 'du', 'duan', 'dui', 'dun', 'duo', 'e', 'er', 'ga', 'gai', 'gan', 'gang', 'gao', 'ge', 'gen', 'geng', 'gong', 'gou', 'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'he', 'hong', 'ji', 'jia', 'jian', 'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'ju', 'juan', 'jue', 'jun', 'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'ken', 'keng', 'kong', 'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo', 'lian', 'lie', 'long', 'lüe', 'luo', 'mie', 'nian', 'nüe', 'nuo', 'pa', 'pai', 'pan', 'pang', 'pao', 'pei', 'pen', 'peng', 'pi', 'pian', 'piao', 'pie', 'pin', 'ping', 'po', 'pou', 'pu', 'qi', 'qia', 'qian', 'qiang', 'qiao', 'qie', 'qin', 'qing', 'qiong', 'qiu', 'qu', 'quan', 'que', 'qun', 'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou', 'ru', 'ruan', 'rui', 'run', 'ruo', 'shi', 'si', 'song', 'sou', 'suo', 'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti', 'tian', 'tiao', 'tie', 'ting', 'tong', 'tou', 'tu', 'tuan', 'tui', 'tun', 'tuo', 'xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing', 'xiong', 'xiu', 'xu', 'xuan', 'xue', 'xun', 'yan', 'ye', 'yi', 'yong', 'you', 'yu', 'yuan', 'yue', 'yun', 'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zei', 'zen', 'zeng', 'zha', 'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhen', 'zheng', 'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui', 'zhun', 'zhuo', 'zi', 'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo' ]
  	 
    wadeGiles = [ 'pa', 'pai', 'pan', 'pang', 'pao', 'pei', 'pen', 'peng', 'pi', 'pien', 'piao', 'pieh', 'pin', 'ping', 'po', 'pu', 'ts`a', 'ts`ai', 'ts`an', 'ts`ang', 'ts`ao', 'ts`e', 'ts`en', 'ts`eng', 'ch`a', 'ch`ai', 'ch`an', 'ch`ang', 'ch`ao', 'ch`e', 'ch`en', 'ch`eng', 'ch`ih', 'ch`ung', 'ch`ou', 'ch`u', 'ch`uai', 'ch`uan', 'ch`uang', 'ch`ui', 'ch`un', 'ch`o', 'tz`u', 'ts`ung', 'ts`ou', 'ts`u', 'ts`uan', 'ts`ui', 'ts`un', 'ts`o', 'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti', 'tien', 'tiao', 'tieh', 'ting', 'tiu', 'tung', 'tou', 'tu', 'tuan', 'tui', 'tun', 'to', 'o', 'erh', 'ka', 'kai', 'kan', 'kang', 'kao', 'ko', 'ken', 'keng', 'kung', 'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kuei', 'kun', 'kuo', 'ho', 'hung', 'chi', 'chia', 'chien', 'chiang', 'chiao', 'chieh', 'chin', 'ching', 'chiung', 'chiu', 'chü', 'chüan', 'chüeh', 'chün', 'k`a', 'k`ai', 'k`an', 'k`ang', 'k`ao', 'k`o', 'k`en', 'k`eng', 'k`ung', 'k`ou', 'k`u', 'k`ua', 'k`uai', 'k`uan', 'k`uang', 'k`uei', 'k`un', 'k`uo', 'lien', 'lieh', 'lung', 'lüeh', 'lo', 'mieh', 'nien', 'nüeh', 'no', 'p`a', 'p`ai', 'p`an', 'p`ang', 'p`ao', 'p`ei', 'p`en', 'p`eng', 'p`i', 'p`ien', 'p`iao', 'p`ieh', 'p`in', 'p`ing', 'p`o', 'p`ou', 'p`u', 'ch`i', 'ch`ia', 'ch`ien', 'ch`iang', 'ch`iao', 'ch`ieh', 'ch`in', 'ch`ing', 'ch`iung', 'ch`iu', 'ch`ü', 'ch`üan', 'ch`üeh', 'ch`ün', 'jan', 'jang', 'jao', 'je', 'jen', 'jeng', 'jih', 'jung', 'jou', 'ju', 'juan', 'jui', 'jun', 'jo', 'shih', 'ssu', 'sung', 'sou', 'so', 't`a', 't`ai', 't`an', 't`ang', 't`ao', 't`e', 't`eng', 't`i', 't`ien', 't`iao', 't`ieh', 't`ing', 't`ung', 't`ou', 't`u', 't`uan', 't`ui', 't`un', 't`o', 'hsi', 'hsia', 'hsien', 'hsiang', 'hsiao', 'hsieh', 'hsin', 'hsing', 'hsiung', 'hsiu', 'hsü', 'hsüan', 'hsüeh', 'hsün', 'yen', 'yeh', 'i', 'yung', 'yu', 'yü', 'yüan', 'yüeh', 'yün', 'tsa', 'tsai', 'tsan', 'tsang', 'tsao', 'tse', 'tsei', 'tsen', 'tseng', 'cha', 'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chih', 'chung', 'chou', 'chu', 'chua', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'cho', 'tzu', 'tsung', 'tsou', 'tsu', 'tsuan', 'tsui', 'tsun', 'tso' ]

    vowels = [ 'a', 'e', 'i', 'o', 'u', 'y' ]

    consonants = [ 'wh', 'th', 'sh', 'ch', 'dj', 'ng', 'p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 's', 'z', 'j', 'w', 'h', 'l', 'r', 'm', 'n' ]

    #for diagnostics...
    #print len(pinYin)
    #print len(wadeGiles)
    #print len(vowels)
    #print len(consonants)

    if selection == 'vowels':
	return vowels
    elif selection == 'consonants':
	return consonants
    elif selection == 'pinYin':
	return pinYin
    elif selection == 'wadeGiles':
	return wadeGiles


def main():
	#for diagnostics...
	print lists('vowels')

if __name__ == '__main__':
	main()
