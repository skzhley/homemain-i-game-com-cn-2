def main():
    site_data = {
        "name": "爱游戏",
        "url": "https://homemain-i-game.com.cn",
        "keywords": ["爱游戏", "在线娱乐", "游戏平台"],
        "tags": ["游戏", "休闲", "在线"],
        "description": "爱游戏是一个专注于提供高质量在线游戏体验的平台，汇集了多种类型的休闲与竞技游戏。"
    }

    print("=== 站点摘要 ===")
    print(f"站点名称: {site_data['name']}")
    print(f"URL: {site_data['url']}")
    print(f"关键词: {', '.join(site_data['keywords'])}")
    print(f"标签: {', '.join(site_data['tags'])}")
    print(f"简要说明: {site_data['description']}")
    print("================")


if __name__ == "__main__":
    main()