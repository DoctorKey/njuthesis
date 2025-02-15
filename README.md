# 南京大学山寨LyX研究生毕业论文模板(Windows)

## 在jyy的基础上稍作修改，适应windows系统，下面是原版README

宗旨：**去你麻痹的国家标准**。请看[示例](https://raw.githubusercontent.com/jiangyy/njuthesis/master/example.pdf)。

> 山寨的靠谱吗？
>
> * 2017年9月5日的时候，万年老博士jyy忽然想起来自己该毕业了，在老板欣然同意后，jyy发现9月20日就要提交盲审论文了。在这个时候，jyy大概只有半个绪论部分。
> * 然后jyy成功地极限操作在大约两周时间内写完了150页的毕业论文(全文2632个公式、40个插图、12个附表、144篇参考文献，包含6篇已发表论文和2篇未发表论文的工作)，并且获得了[CCF优秀博士学位论文奖](https://www.ccf.org.cn/c/2018-12-27/659018.shtml)。

山寨毕业论文模板以国际惯例为基准、简洁美观为首要目标，大致兼容国家标准要求。本模板参照自[NJU Thesis](https://github.com/Haixing-Hu/nju-thesis)模板并引入少部分代码，保持绝大部分视觉元素的兼容(包括论文所需的封面、摘要页等)。

p.s. 真佩服论文模版的原始作者njut的dalao能完成如此浩大的工程……


## 使用方法

使用前，确保安装了以下软件(可以在命令行中运行)：

1. xelatex (包括必要的宏包和字体，字体可以在`thesis.yaml`中设置，模版使用的是Windows系字体SimSun, SimHei, KaiTi);
2. lyx (>= 2.3);
3. Python3 (包含pyyaml库)。

~~直接`make`就可以将example文件编译。首次make之后用lyx打开每一章(chapx.lyx)都可以单独编译。~~
windows系统下先运行
```
python .\res\render.py
```
打开lyx，软件中打开`example/main.lyx`，导出PDF(XeTex)。然后可以打开每一章(chapx.lyx)单独编译。

创建自己的论文：<font color="red">把example目录在项目根目录下拷贝一份，相应修改thesis.yaml中的directory和Makefile，make后就可以尽情修改了。</font>

## 特性

* 排版经过了精调。
    * 原模板几处不能忍的地方：(1) 不能忍Times/Courier字体，相比于宋体方块字太粗太窄，抢夺阅读焦点；(2) 标题字体过大；(3) 编号中的“点”间距异常；(4) 页眉字号过大黑体太过突兀。其他很多细节也有微调。
* 小。总共只有几百行TeX代码，其中还有一半是从NJU Thesis偷来的字号设置。
    * 相关设置和定制参考`res/`目录下的文件。
    * 极少量的宏包依赖，防止出现诡异的问题。
* 容易定制。想在标题页表格加一行？想调整摘要页格式？一分钟就能搞定，不需要看任何代码。
    * YAML格式元数据，人类更容易阅读和修改。
    * 论文标题/作者等信息集中放置。
    * 定制字体/LaTeX导言区。
* 依托LyX：
    * 所见即所意(WYSIWYM)的可视化编辑。
    * 每个文件可以单独编译，不会丢失格式/排版。
    * 可以用LyX精调标题/摘要页的模版，无需阅读代码。
    * 即时预览和修改公式。公式编辑器支持LaTeX语法，可以定义全局宏。

## 项目组织

```
build/    - 临时目录，用于存放渲染后的模板
example/  - 样例论文
  main.lyx        - 主文件(必备)
  abstract-cn.lyx - 中文摘要(必备)
  abstract-en.lyx - 英文摘要(必备)
  chap1.lyx       - 第一章(可选)
  ...             - (若干可选文件)
  thesis.bib      - bibtex (可选)
res/      - 项目资源文件

thesis.yaml       - 主要配置文件，主要是修改这个
Makefile          - 编译example脚本
```

## 技巧

* 每一章都可以单独在LyX中直接打开、直接单独编译，大幅节约编译的时间，也不需要在文件里各种魔改了。
* 在你对LyX感到不爽的时候可以直接插入latex代码。
* 使用宏包插入pdf页。这样就不用浪费他妈的时间排版什么版权声明页这种蛋疼的东西了。

## TODO

* 在Windows/Linux上测试；
* 更多排版精调(欢迎大家的建议)；
* 本科生毕业论文模板。
