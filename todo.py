import requests
import json
import time

def get_video_info(bv_id):
    api_url = f'https://api.bilibili.com/x/web-interface/view?bvid={bv_id}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data['code'] == 0:
            video_info = data['data']
            title = video_info['title']
            description = video_info['desc']
            view_count = video_info['stat']['view']
            danmaku_count = video_info['stat']['danmaku']
            like_count = video_info['stat']['like']
            return {
                'BV号': bv_id,
                '标题': title,
                '描述': description,
                '观看量': view_count,
                '弹幕数': danmaku_count,
                '点赞数': like_count
            }
        else:
            return {
                'BV号': bv_id,
                '错误': '获取视频信息失败'
            }
    except requests.exceptions.RequestException as e:
        return {
            'BV号': bv_id,
            '错误': str(e)
        }

bv_ids = [
    'BV197421f7BY', 'BV1Lf42197qm', 'BV18M4m1z7MK',
    'BV1uZ421g75S', 'BV1vw4m1e7h2', 'BV1rz421B7PZ',
    'BV14f421B7pD', 'BV1zf421z7Jc'
]

videos_info = []
for bv_id in bv_ids:
    info = get_video_info(bv_id)
    videos_info.append(info)
    # 控制请求频率，避免被阻止
    time.sleep(1)

with open('bilibili_videos.json', 'w', encoding='utf-8') as f:
    json.dump(videos_info, f, ensure_ascii=False, indent=4)
