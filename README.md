# NodeCAD 建筑节点与大样助手

NodeCAD 是面向建筑节点分析与 CAD 绘图的 AI 技能，可用于参考图识读、授权图集与规范线索检索、构造层次分析，以及节点大样的绘制和检查。技能支持 WorkBuddy 格式，也可由支持 SKILL.md 的智能体按其规则加载。

## 1.2.0 离线使用

下载 [WorkBuddy 导入包](nodecad-workbuddy.zip)，在 WorkBuddy 技能页上传 ZIP。用于 Codex 时，下载 [Codex 技能包](nodecad-codex.zip)，将包内的 nodecad 目录放入技能目录。头像可单独取用 [512 px PNG](nodecad-avatar.png)。

首次试用可以直接说「没有本地图集，画一个干区地砖接浮铺木地板的剖面。两侧构造厚均为 45 mm，标出木侧净缝和盖条搭接」。包内有可调整的示例参数、室内和外围护构造指南、连续尺寸链和纸面表达方法。仅做构造分析、尺寸复核或审图时，直接读取技能即可。

## 离线出图

解压后在 nodecad 目录运行。地材交接 SVG 只需 Python 3.11+，使用系统浏览器即可打开。两个屋面 DXF 示例另需安装 scripts/requirements.txt 中的 ezdxf。

```bash
python scripts/floor_section.py --params examples/floor-study.json --out floor.svg
python scripts/nodecad.py --params examples/parapet-test.json --out parapet.dxf
python scripts/detail_redraw.py --config examples/flashing-study-test.json --out flashing.dxf
```

参数文件采用演示工况。墙身、窗洞、灯槽、门套、湿区及地下节点可用包内方法按项目分析、审图或另行绘制。详图做法引用、产品性能、标准现行性和出图比例须结合对应原页、设备和项目核验。包内提供原创方法和引用线索，第三方图集、规范原文、工程图纸和字体由使用者按需取得。

## 许可

代码和本仓库原创文档采用 MIT 许可，见 `LICENSE`。第三方依赖分别遵循各自许可；生成头像作为本项目附带资产提供。示例数字仅为测试假设。
