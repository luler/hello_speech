import os.path
import re
import shutil
import uuid

from flask import request

# 测试接口
from tool import common, speech_tool
from tool.valid_tool import valid_tool


def test():
    return common.json_return('访问成功')


# 文本转语音
def tts():
    filed = ['text', 'am', ]
    param = common.get_request_param(filed)
    valid_tool.checkData(param, {
        'text|文本': 'required'
    })
    am = param.get('am', 'fastspeech2_csmsc')
    if am not in ['speedyspeech_csmsc', 'fastspeech2_csmsc', 'fastspeech2_aishell3', 'fastspeech2_ljspeech',
                  'fastspeech2_vctk', ]:
        # 参考：https://gitee.com/paddlepaddle/PaddleSpeech/tree/develop/demos/text_to_speech
        raise Exception('声学模型不存在')
    data = {
        'speedyspeech_csmsc': {
            'voc': 'mb_melgan_csmsc',
            'lang': 'zh',
        },
        'fastspeech2_csmsc': {
            'voc': 'pwgan_csmsc',
            'lang': 'zh',
        },
        'fastspeech2_aishell3': {
            'voc': 'pwgan_aishell3',
            'lang': 'zh',
        },
        'fastspeech2_ljspeech': {
            'voc': 'pwgan_ljspeech',
            'lang': 'en',
        },
        'fastspeech2_vctk': {
            'voc': 'pwgan_vctk',
            'lang': 'en',
        },
    }
    res = {}
    res['output_wav'] = speech_tool.tts(param['text'], am, data[am]['voc'], data[am]['lang'])
    return common.json_return('语音合成完成', res)


# 语音识别
def asr():
    filed = ['model', ]
    param = common.get_request_param(filed)
    model = param.get('model', 'conformer_wenetspeech')
    if model not in ['conformer_wenetspeech', 'conformer_online_multicn', 'conformer_aishell',
                     'conformer_online_aishell',
                     'transformer_librispeech', 'deepspeech2online_wenetspeech', 'deepspeech2offline_aishell',
                     'deepspeech2online_aishell', 'deepspeech2offline_librispeech', ]:
        # 参考：https://gitee.com/paddlepaddle/PaddleSpeech/tree/develop/demos/speech_recognition
        raise Exception('声学模型不存在')
    file = request.files.get('wav_file')
    if file == None:
        raise Exception('声音文件不能为空')
    ext = re.search(".([a-z|A-Z]*?)$", file.filename).group(1).lower()
    if ext not in ['wav', ]:
        raise Exception('不支持当前文件后缀名')
    prefix = 'static/asr_file/'
    if os.path.exists(prefix) == False:
        os.mkdir(prefix)
    filename = prefix + str(uuid.uuid1()) + '.' + ext
    file.save(filename)
    # 很坑，f.read在f.save前，保存的文件会是空的
    last_file = prefix + common.md5_file(filename) + '.' + ext
    shutil.move(filename, last_file)
    data = {
        'conformer_wenetspeech': {
            'lang': 'zh',
        },
        'conformer_online_multicn': {
            'lang': 'zh',
        },
        'conformer_aishell': {
            'lang': 'zh',
        },
        'conformer_online_aishell': {
            'lang': 'zh',
        },
        'deepspeech2online_wenetspeech': {
            'lang': 'zh',
        },
        'deepspeech2offline_aishell': {
            'lang': 'zh',
        },
        'deepspeech2online_aishell': {
            'lang': 'zh',
        },
        'transformer_librispeech': {
            'lang': 'en',
        },
        'deepspeech2offline_librispeech': {
            'lang': 'en',
        },
    }
    res = {}
    res['result_text'] = speech_tool.asr(last_file, model, data[model]['lang'])
    return common.json_return('语音识别完成', res)


# 标点恢复
def punctuation():
    filed = ['model', 'text']
    param = common.get_request_param(filed)
    valid_tool.checkData(param, {
        'text|文本': 'required'
    })
    model = param.get('model', 'ernie_linear_p3_wudao')
    if model not in ['ernie_linear_p3_wudao', 'ernie_linear_p7_wudao', ]:
        # 参考：https://gitee.com/paddlepaddle/PaddleSpeech/tree/develop/demos/punctuation_restoration
        raise Exception('标点模型不存在')
    data = {
        'ernie_linear_p3_wudao': {
            'lang': 'zh',
        },
        'ernie_linear_p7_wudao': {
            'lang': 'zh',
        },
    }
    res = {}
    res['result_text'] = speech_tool.punctuation(param['text'], model, data[model]['lang'])
    return common.json_return('标点恢复完成', res)
