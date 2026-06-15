"""本地配置文件管理

使用 JSON 格式保存程序配置，文件位于程序目录下的 config.json。
"""

import json
import os
from typing import Optional

_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

_default_config = {
    'game_path': '',
}


def load() -> dict:
    """加载配置文件，不存在则返回默认配置"""
    if not os.path.exists(_CONFIG_PATH):
        return dict(_default_config)
    try:
        with open(_CONFIG_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 合并默认值（新增字段自动补全）
        result = dict(_default_config)
        result.update(data)
        return result
    except Exception:
        return dict(_default_config)


def save(cfg: dict):
    """保存配置到文件"""
    with open(_CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def get_game_path() -> str:
    """获取游戏路径"""
    return load().get('game_path', '')


def set_game_path(path: str):
    """设置游戏路径"""
    cfg = load()
    cfg['game_path'] = path
    save(cfg)
