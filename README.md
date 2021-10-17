
# okteto-nb2
[![tests](https://github.com/ffreemt/okteto-nb2/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/okteto-nb2/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.7.3%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Run/test/develop plugins for nonebot2 + cqhttp in `okteto`, agilely

## Install `okteto cli`

*   register 注册 `okteto`: [https://okteto.com/](https://okteto.com/)
*   install 安装`okteto cli`: [https://okteto.com/docs/getting-started/installation/](https://okteto.com/docs/getting-started/installation/)

## Use it
*   setup 设置`go-cqhttp`
    ```bash
    git clone https://github.com/ffreemt/okteto-nb2.git
    cd okteto-nb2 && cd go-cqhttp
    # 下载 `go-cqhttp`
    # 例如 wget -c https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-beta7-fix2/go-cqhttp_linux_amd64.tar.gz && tar fvzx go-cqhttp_linux_amd64.tar.gz go-cqhttp
    # 设置 `config.yml` (参看`config.yml-`) 和生成 `device.json` (参看`go-cqhttp`文档及 https://github.com/Mrs4s/go-cqhttp/blob/master/docs/slider.md）
    ```
*   login to 登录 `okteto`
    ```bash
    # docker login  # not readlly needed for the whole thing to work
    okteto login
    ```
*   run 运行 `okteto up`
    ```bash
    cd ..  # cd okteto-nb2
    okteto up
    ```
    enter 进入 `okteto`， run 运行
    ```bash
    app> apt-get install -y supervisor
    app> supervisord -c gocqhttp.conf  # start go-cqhttp

    app> pip install poetry --disable-pip-version-check && poetry install --no-dev --no-interaction --no-ansi  # install packages
    app> poetry run python bot.py
    # or poetry run uvicorn --host 0.0.0.0 --port 8680 bot:app --reload --reload-dir okteto_nb2

    ...[INFO] nonebot | WebSocket Connection from CQHTTP Bot 2129462094 Accepted!
    INFO:     connection open
    ```

    检测是否正常运行: 本机另开终端运行
    ```
    curl 127.0.0.1:8680
    # {"success":"Hello nb2chan! "}

    curl "127.0.0.1:8680/nb2chan/?Token=DEMO_TOKEN&qq=1234msg=okteto-msg"

    # {"error":"okteto-nb2-55d5d887cb-2p6r5 exc: <NetWorkError message=WebSocket API call timeout>, (大佬这个qq号[1234]加机器人好友了吗？ 没加的话用不了nb2酱。)"}
    ```

    Happy coding……快乐地码码……

## More coming soon...