
# okteto-nb2
[![tests](https://github.com/ffreemt/okteto-nb2/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/okteto-nb2/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.7.3%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Run/test/develop plugins for nonebot2 + cqhttp in `okteto`, agilely

## Install `okteto cli`

*   register 注册 `okteto`: [https://okteto.com/](https://okteto.com/)
*   install 安装`okteto cli`: [https://okteto.com/docs/getting-started/installation/](https://okteto.com/docs/getting-started/installation/)

## Use it
*   setup 设置`go-cqhttp`
    ```bash
    cd go-cqhttp
    # 下载 `go-cqhttp`
    # 例如 wget -c https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-beta7-fix2/go-cqhttp_linux_amd64.tar.gz && tar fvzx go-cqhttp_linux_amd64.tar.gz go-cqhttp
    # 设置 `config.hjson` (参看`config.hjson-`) 和生成 `device.json` (参看`go-cqhttp`文档及 https://github.com/Mrs4s/go-cqhttp/blob/master/docs/slider.md）
    ```
*   login to 登录 `okteto`
    ```bash
    docker login  # needed for the whole thing to work
    okteto login
    ```
*   run 运行
    ```bash
    cd okteto-nb2
    okteto up
    ```

    Happy coding……快乐地码码……

## More coming soon...