import threading
import uuid
import paddle
from flask import current_app
from paddlespeech.cli import TTSExecutor, ASRExecutor, TextExecutor


# 文本转语音
def tts(text, am='fastspeech2_csmsc', voc='pwgan_csmsc', lang='zh'):
    key = am + voc + lang + '_' + str(threading.currentThread().ident)
    if hasattr(current_app, 'tts') == False:
        current_app.tts = {}
    if key not in current_app.tts:
        speech = TTSExecutor()
        speech(
            text='初始化',
            output='static/temp.wav',
            am=am,
            am_config=None,
            am_ckpt=None,
            am_stat=None,
            spk_id=0,
            phones_dict=None,
            tones_dict=None,
            speaker_dict=None,
            voc=voc,
            voc_config=None,
            voc_ckpt=None,
            voc_stat=None,
            lang=lang,
            device=paddle.get_device()
        )
        current_app.tts[key] = speech

    speech = current_app.tts[key]

    output_file = 'static/' + str(uuid.uuid1()) + '.wav'
    speech.infer(text=text, lang=lang, am=am)
    speech.postprocess(output=output_file)

    return '/' + output_file


# 自动语音识别
def asr(audio_file, model='conformer_wenetspeech', lang='zh'):
    key = model + lang + '_' + str(threading.currentThread().ident)
    if hasattr(current_app, 'asr') == False:
        current_app.asr = {}
    if key not in current_app.asr:
        asr_executor = ASRExecutor()
        asr_executor(
            model=model,
            lang=lang,
            sample_rate=16000,
            config=None,  # Set `config` and `ckpt_path` to None to use pretrained model.
            ckpt_path=None,
            audio_file='temp.wav',
            force_yes=True,
            device=paddle.get_device()
        )
        current_app.asr[key] = asr_executor

    asr_executor = current_app.asr[key]

    asr_executor.preprocess(model, audio_file)
    asr_executor.infer(model)
    text = asr_executor.postprocess()

    return text


# 标点恢复
def punctuation(text, model='ernie_linear_p3_wudao', lang='zh'):
    key = model + lang + '_' + str(threading.currentThread().ident)
    if hasattr(current_app, 'punctuation') == False:
        current_app.punctuation = {}
    if key not in current_app.punctuation:
        executor = TextExecutor()
        executor(
            text=text,
            task='punc',
            model=model,
            lang=lang,
            config=None,
            ckpt_path=None,
            punc_vocab=None,
            device=paddle.get_device()
        )
        current_app.punctuation[key] = executor

    executor = current_app.punctuation[key]

    executor.preprocess(text)
    executor.infer()
    text = executor.postprocess()

    return text
