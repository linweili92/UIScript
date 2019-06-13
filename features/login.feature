#language: zh-CN
功能: 登录验证

  场景: 正常登录操作
    当 启动APP
    假如 点击底部的我
    当 选择正式环境
    那么 重新启动APP
    假如 未登录
    假如 点击底部的我
    那么 点击我|请登录账户
    那么 点击我|手机登录
    当 在我|请输入手机号键入18229365263
    当 在我|请输入密码键入123456
    那么 点击我|登录
    假如 检查到我|用户名相关信息
    那么 标记登录成功

  场景: 进行退出登录操作
    假如 已登录
    假如 点击底部的我
    那么 点击我|设置
    那么 点击我|退出登录
    假如 检查到我|请登录账户相关信息
    那么 标记退出登录成功

  场景: 访问一级菜单
    假如 已登录




