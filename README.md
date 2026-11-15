# NodeCAD 建筑节点与大样助手

NodeCAD 是面向建筑节点分析与 CAD 绘图的 AI 技能，可用于参考图识读、授权图集与规范线索检索、构造层次分析，以及节点大样的绘制和检查。技能支持 WorkBuddy 格式，也可由支持 SKILL.md 的智能体按其规则加载。

## 功能

- 分析屋面、墙身、地下防水、穿墙管和楼地面等节点的材料层次、连接、收头和排水关系。
- 结合用户授权的资料定位图号、页码和引用，并组织剖面、填充、引线、尺寸及图名。
- 内置两个 DXF 原型脚本：女儿墙示意、一类屋面泛水研究图。其他节点须结合图纸和环境逐项实现。
- 在条件允许时辅助检查 CAD 的字体、尺寸、图块、裁剪、填充和打印；报告依据与未核问题。

## WorkBuddy 导入

下载仓库中的 `nodecad-workbuddy.zip`，在 WorkBuddy 的技能页面选择添加、上传技能并选择该文件。图标在 `nodecad-avatar.png`（压缩包内也含有头像），如界面要求可单独上传。不同客户端的功能与名称可能有所差异。

## 脚本运行

先下载并解压 `nodecad-workbuddy.zip`；其中包含 `nodecad/` 源码目录。需要 Python 3.11+ 和 `ezdxf`，在有授权的环境中安装 `nodecad/scripts/requirements.txt`。在解压后的目录运行以下示例；参数完全虚构，仅供检查脚本，不代表实际工程条件：

```bash
python nodecad/scripts/nodecad.py --params nodecad/examples/parapet-test.json --out parapet-test.dxf
python nodecad/scripts/detail_redraw.py --config nodecad/examples/flashing-study-test.json --out flashing-test.dxf
```

DXF 文字显示依赖目标 CAD 中可用的字体；请按需修改配置。项目没有附带 AutoCAD、图集、规范正文或用户工程图。

## 重要边界

两个脚本只生成指定范围的研究原型，不提供任意节点一键成图。需要明确项目条件、核对现行依据、目标 CAD 显示和实际打印比例；尺寸或填充是否关联需逐项验证。成果应由有资质的设计人员审查，不能直接当作施工图。

## 许可

代码和本仓库原创文档采用 MIT 许可，见 `LICENSE`。第三方依赖分别遵循各自许可；生成头像作为本项目附带资产提供。示例数字仅为测试假设。
